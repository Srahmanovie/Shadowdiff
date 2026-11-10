import os
import requests

def post_pr_comment(repo_slug: str, pr_number: int, analysis_results: list):
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set.")
        return

    total_risks = sum(len(res["heuristics"]) + len(res["ast"]) for res in analysis_results)
    if total_risks == 0:
        comment_body = "✅ **ShadowDiff Sentinel:** No suspicious behavioral changes or supply chain anomalies detected in this PR."
    else:
        comment_body = "🚨 **ShadowDiff Security Warning:** Potential supply chain risks or malicious patterns detected!\n\n"
        comment_body += "| File Path | Vulnerability Type | Details |\n"
        comment_body += "| :--- | :--- | :--- |\n"
        
        for res in analysis_results:
            file_path = res["file"]
            for h in res["heuristics"]:
                comment_body += f"| `{file_path}` | Heuristic Match | {h} |\n"
            for a in res["ast"]:
                comment_body += f"| `{file_path}` | AST Analysis | {a} |\n"
                
        comment_body += "\n*Please review the highlighted code blocks manually before merging.*"

    # Post to GitHub API
    url = f"https://api.github.com/repos/{repo_slug}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }
    payload = {"body": comment_body}
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print("Successfully posted security report to GitHub PR.")
    else:
        print(f"Failed to post comment: {response.status_code} - {response.text}")
