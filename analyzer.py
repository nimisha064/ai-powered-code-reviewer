
import ast


def analyze_code(code):
    """Analyze Python code for selected quality issues."""
    issues = []

    try:
        tree = ast.parse(code)
    except SyntaxError as error:
        issues.append({
            "severity": "critical",
            "line": error.lineno,
            "message": f"Syntax error: {error.msg}",
        })
        return issues

    assigned_variables = {}

    # Check functions without docstrings.
    for node in ast.walk(tree):
        if (
            isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and ast.get_docstring(node) is None
        ):
            issues.append({
                "severity": "low",
                "line": node.lineno,
                "message": (
                    f"Function '{node.name}' has no documentation."
                ),
            })

    # Collect simple variable assignments.
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                for item in ast.walk(target):
                    if isinstance(item, ast.Name):
                        assigned_variables.setdefault(
                            item.id, node.lineno
                        )

        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
        ):
            assigned_variables.setdefault(
                node.target.id, node.lineno
            )

    # Find names that are read in the code.
    used_variables = {
        node.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Name)
        and isinstance(node.ctx, ast.Load)
    }

    # Report potentially unused variables.
    for name, line in assigned_variables.items():
        if name not in used_variables and not name.startswith("_"):
            issues.append({
                "severity": "medium",
                "line": line,
                "message": f"Variable '{name}' may be unused.",
            })

    return sorted(
        issues,
        key=lambda issue: (
            issue["line"] if issue["line"] is not None else 0
        ),
    )


if __name__ == "__main__":
    sample_code = """
def greet():
    message = "Hello"
"""

    for issue in analyze_code(sample_code):
        print(
            f"[{issue['severity'].upper()}] "
            f"Line {issue['line']}: {issue['message']}"
        )
