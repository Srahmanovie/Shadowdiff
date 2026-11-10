import ast

class BehavioralVisitor(ast.NodeVisitor):
    def __init__(self):
        self.risk_score = 0
        self.findings = []

    def visit_Call(self, node):
        # Check for dangerous built-in functions
        if isinstance(node.func, ast.Name):
            if node.func.id in ['eval', 'exec']:
                self.findings.append(f"Critical: Use of dangerous dynamic execution ({node.func.id}) at line {node.lineno}")
                self.risk_score += 10

        # Check for outbound network or subprocess execution attempts
        elif isinstance(node.func, ast.Attribute):
            if node.func.attr in ['urlopen', 'socket', 'system', 'popen']:
                self.findings.append(f"Warning: Potential system/network access call ({node.func.attr}) at line {node.lineno}")
                self.risk_score += 5

        self.generic_visit(node)
