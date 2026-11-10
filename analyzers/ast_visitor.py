import ast

class AdvancedBehavioralVisitor(ast.NodeVisitor):
    def __init__(self):
        self.risk_score = 0
        self.findings = []
        self.imported_modules = set()

    def visit_Import(self, node):
        for alias in node.names:
            self.imported_modules.add(alias.name)
            if alias.name in ['pickle', 'marshal', 'ctypes', 'subprocess']:
                self.findings.append(f"High Risk: Dangerous module import ({alias.name}) at line {node.lineno}")
                self.risk_score += 8
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module in ['os', 'sys', 'subprocess', 'socket']:
            for alias in node.names:
                self.findings.append(f"Medium Risk: System-level import from {node.module}: {alias.name} at line {node.lineno}")
                self.risk_score += 4
        self.generic_visit(node)

    def visit_Call(self, node):
        # Catch eval, exec, compile
        if isinstance(node.func, ast.Name):
            if node.func.id in ['eval', 'exec', 'compile', 'globals', 'locals']:
                self.findings.append(f"Critical: Execution/Reflection sink used ({node.func.id}) at line {node.lineno}")
                self.risk_score += 15

        # Catch dynamic attribute calls (e.g., getattr(os, 'system')('cmd'))
        elif isinstance(node.func, ast.Name) and node.func.id == 'getattr':
            self.findings.append(f"High Risk: Dynamic attribute resolution (getattr) detected at line {node.lineno}")
            self.risk_score += 10

        # Catch outbound networking / shell execution
        elif isinstance(node.func, ast.Attribute):
            if node.func.attr in ['urlopen', 'socket', 'Popen', 'system', 'run', 'getoutput']:
                self.findings.append(f"High Risk: Outbound network or shell command trigger ({node.func.attr}) at line {node.lineno}")
                self.risk_score += 10

        self.generic_visit(node)
