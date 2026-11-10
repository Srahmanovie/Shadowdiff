# Contributing to ShadowDiff 🛡️

First off, thank you for taking the time to contribute! Security supply chain tools thrive on community-driven rules, heuristics, and platform integrations.

## Code of Conduct
By participating, you are expected to uphold our open-source community standards. Be respectful, constructive, and collaborative.

---

## How Can I Contribute?

### 1. Reporting Bugs & Requesting Features
* **Found a false positive or evasion technique?** Open an issue with a clear code example.
* **Want a new language parser?** (e.g., Go, Ruby, Rust), open a feature request issue to discuss architecture before coding.

### 2. Submitting Pull Requests
1. **Fork the repository** and create your feature branch from `main`:
   ```bash
   git checkout -b feature/amazing-detection-rule

2. Install dependencies and set up your local environment:
    pip install -r requirements.txt

3. Write or update analyzer rules in the respective analyzers/ module (e.g., js_analyzer.py or ast_visitor.py).

4. Test locally against sample malicious and benign files to ensure zero false positives.

5.Commit your changes with clear commit messages:
   git commit -m "feat(analyzer): add detection for dynamic eval evasion in JS"

6. Push to your fork and submit a Pull Request to main.

🧩 Adding New AST or Heuristic Rules
​When adding a new rule to either the Python AST visitor or the JS analyzer:
​Include a test case demonstrating both the malicious pattern it catches and a clean version that it won't flag (to prevent false positives).
​Document the risk level clearly (e.g., Critical, High, Medium) based on potential for data exfiltration or arbitrary code execution.
​Thank you for helping make open-source software supply chains safer! 🚀
