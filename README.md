<div align="center">

# 🛡️ ShadowDiff
### *Catch Supply Chain Backdoors & Malicious Dependency Diffs Before They Reach Production.*

[![GitHub Release](https://img.shields.io/github/v/release/srahmanovie/shadowdiff?style=for-the-badge)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)]()

</div>

---

Modern supply chain attacks don't look like blatant malware—they look like minor version bumps that quietly execute `eval()`, scrape environment variables, or exfiltrate secrets via hidden outbound requests during build steps.

**ShadowDiff** performs deep behavioral AST diffing and heuristic analysis on pull requests to flag hidden malicious code introduced in third-party dependency updates.

---

## ⚡ Key Features

* **🧠 Behavioral AST Parsing:** Detects dynamic execution (`eval`, `exec`), reflection (`getattr`), and suspicious system imports instead of relying solely on signature matching.
* **🕵️ Exfiltration Pattern Detection:** Spots unauthorized environment variable reads combined with outbound network requests.
* **💬 Automated PR Security Comments:** Injects clean, color-coded Markdown risk tables directly into your GitHub Pull Requests.
* **🚀 Zero-Config CI/CD:** Drop it into GitHub Actions in under 2 minutes.

---

## 🛠️ Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/srahmanovie/shadowdiff.git
   cd shadowdiff

2. Install dependencies 
   pip install -r requirements.txt

3. Run a local scan
   python cli.py --repo "your-org/your-repo" --pr 42



