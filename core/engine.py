from core.diff_parser import get_dependency_changes
from analyzers.ast_visitor import BehavioralVisitor
from analyzers.heuristics import scan_code_string
import ast

def run_analysis(pr_diff_files):
    report = []
    for file_path, added_code in pr_diff_files.items():
        if not file_path.endswith(('.py', '.js', '.ts')):
            continue
            
        # Run heuristic check
        heuristics_found = scan_code_string(added_code)
        
        # Run AST check if Python
        ast_findings = []
        if file_path.endswith('.py'):
            try:
                tree = ast.parse(added_code)
                visitor = BehavioralVisitor()
                visitor.visit(tree)
                ast_findings = visitor.findings
            except SyntaxError:
                pass # Partial diff chunks might cause syntax errors

        if heuristics_found or ast_findings:
            report.append({
                "file": file_path,
                "heuristics": heuristics_found,
                "ast": ast_findings
            })
            
    return report
