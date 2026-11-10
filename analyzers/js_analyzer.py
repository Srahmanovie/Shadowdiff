import re

JS_RISK_PATTERNS = [
    # Dangerous execution sinks
    (r"\beval\s*\(", "Critical: Use of dynamic eval()"),
    (r"new\s+Function\s*\(", "Critical: Dynamic Function constructor execution"),
    
    # Process / System execution (Node.js)
    (r"child_process\s*\.\s*(exec|execSync|spawn|fork)", "High Risk: Spawning shell processes via child_process"),
    (r"require\s*\(\s*['\"]child_process['\"]", "High Risk: Importing child_process module"),
    
    # Obfuscation & Evasion
    (r"Buffer\.from\s*\(.+,\s*['\"]base64['\"]", "Medium Risk: Base64 decoding (potential payload obfuscation)"),
    (r"atob\s*\(", "Medium Risk: Using atob() for decoding strings"),
    
    # Network / Exfiltration
    (r"(axios|fetch|http|https)\s*\.\s*(post|get)\s*\(.+process\.env", "Critical: Environment variables passed into network request"),
]

def scan_js_code(code_content: str):
    findings = []
    risk_score = 0
    
    for pattern, description in JS_RISK_PATTERNS:
        matches = re.findall(pattern, code_content)
        if matches:
            findings.append(description)
            risk_score += 8
            
    return findings, risk_score
