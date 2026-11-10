import re

RISK_PATTERNS = [
    (r"os\.environ", "Accesses environment variables"),
    (r"base64\.b64encode", "Potential data encoding/exfiltration pattern"),
    (r"requests\.(post|get)\(.*?(token|key|secret)", "Possible credential transmission in web request"),
    (r"subprocess\.check_output", "Executes shell commands")
]

def scan_code_string(code_content: str):
    detected_risks = []
    for pattern, description in RISK_PATTERNS:
        if re.search(pattern, code_content, re.IGNORECASE):
            detected_risks.append(description)
    return detected_risks
