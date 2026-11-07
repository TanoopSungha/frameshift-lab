"""Open a metadata-only GitLab MR when tracked public GitHub heads move."""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / "upstream-lock.json"
TOKEN = os.getenv("GITLAB_UPDATE_TOKEN")
if not TOKEN:
    print("GITLAB_UPDATE_TOKEN is not configured; skipping upstream review job.")
    sys.exit(0)

api = os.getenv("CI_API_V4_URL", "https://gitlab.com/api/v4")
project = urllib.parse.quote(os.environ["CI_PROJECT_PATH"], safe="")
def request(url, method="GET", data=None):
    payload = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=payload, method=method, headers={"PRIVATE-TOKEN": TOKEN, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response) if response.status != 204 else {}

lock = json.loads(LOCK.read_text())
previous = lock.get("heads", {})
current = {}
for repo in lock["repositories"]:
    url = f"https://api.github.com/repos/{repo}/commits?per_page=1"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "FrameShift-Lab-upstream-review"})
    with urllib.request.urlopen(req, timeout=30) as response:
        commits = json.load(response)
    current[repo] = commits[0]["sha"] if commits else ""

changed = {repo: sha for repo, sha in current.items() if previous.get(repo) != sha}
if not changed:
    print("Tracked upstream heads are unchanged.")
    sys.exit(0)
lock["heads"] = current
lock["checked_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
branch = "upstream-review-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
project_api = f"{api}/projects/{project}"
request(f"{project_api}/repository/branches?branch={urllib.parse.quote(branch)}&ref={urllib.parse.quote(os.environ['CI_DEFAULT_BRANCH'])}", "POST")
request(f"{project_api}/repository/commits", "POST", {
    "branch": branch,
    "commit_message": "chore: record upstream commit changes for review",
    "actions": [{"action": "update" if previous else "update", "file_path": "upstream-lock.json", "content": json.dumps(lock, indent=2) + "\n"}]
})
summary = "\n".join(f"- `{repo}`: `{previous.get(repo, 'not recorded')[:12]}` → `{sha[:12]}`" for repo, sha in changed.items())
request(f"{project_api}/merge_requests", "POST", {
    "source_branch": branch,
    "target_branch": os.environ["CI_DEFAULT_BRANCH"],
    "title": "Review upstream project updates",
    "description": "The scheduled check detected upstream commit changes. This proposal updates commit pointers only; it does not copy or merge upstream code. Review project activity, releases, licenses, and catalog accuracy before merging.\n\n" + summary,
    "remove_source_branch": True
})
print(f"Opened metadata-only review MR for {len(changed)} upstream project(s).")
