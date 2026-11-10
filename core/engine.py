import ast
from analyzers.ast_visitor import AdvancedBehavioralVisitor
from analyzers.js_analyzer import scan_js_code

def run_analysis(pr_diff_files):
    report = []
    
    for file_path, code_content in pr_diff_files.items():
        heuristics_found = []
        ast_findings = []
        
        # Python Files
        if file_path.endswith('.py'):
            try:
                tree = ast.parse(code_content)
                visitor = AdvancedBehavioralVisitor()
                visitor.visit(tree)
                ast_findings = visitor.findings
            except SyntaxError:
                pass # Handle partial diff chunks gracefully
                
        # JavaScript / TypeScript Files
        elif file_path.endswith(('.js', '.ts', '.jsx', '.tsx', '.mjs')):
            js_findings, score = scan_js_code(code_content)
            ast_findings.extend(js_findings)

        if ast_findings:
            report.append({
                "file": file_path,
                "heuristics": heuristics_found,
                "ast": ast_findings
            })
            
    return report
