# AI-Powered Code Reviewer & Quality Analyzer

## Overview

The AI-Powered Code Reviewer & Quality Analyzer is a Python-based static code analysis project that identifies selected code-quality issues using Python's Abstract Syntax Tree (AST).

The project aims to explore how lightweight program analysis can help developers identify common coding issues and improve code readability and maintainability.

## Features

- **Syntax Error Detection:** Identifies Python syntax errors and reports the error location.
- **Missing Documentation Detection:** Finds functions that do not have docstrings.
- **Potentially Unused Variables:** Flags certain assigned variables that are not read in the analyzed code.
- **Severity Classification:** Categorizes detected issues as critical, medium, or low.
- **Automated Testing:** Includes unit tests to check the analyzer's basic functionality.

## Technologies Used

- Python
- Abstract Syntax Tree (AST)
- Python `unittest`
- Ruff for code-quality checks

## Project Structure

```text
AI-Code-Reviewer/
├── backend/
│   ├── analyzer.py
│   └── test_analyzer.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.10 or later

### Run the Analyzer

Open a terminal in the project directory and run:

```bash
python backend/analyzer.py
```

### Run Unit Tests

```bash
python -m unittest discover -s backend -p "test_*.py" -v
```

### Run Ruff Checks

If Ruff is installed, run:

```bash
python -m ruff check backend
```

## Testing

The project includes four unit tests covering:

1. Valid Python code.
2. Syntax error detection.
3. Missing function docstrings.
4. Potentially unused variables.

All four tests passed in the local test run.

## Research Direction

A possible next step is to compare the analyzer's findings with an established static-analysis tool using a labeled set of Python code examples. This could help evaluate detection accuracy, identify false positives, and understand the limitations of lightweight AST-based analysis.

## Limitations

- The analyzer checks only a limited set of code-quality issues.
- The unused-variable check is heuristic and may produce false positives or miss some cases.
- The project does not currently use a machine-learning model or an LLM to review code.
- No comparative accuracy results have been established yet.

## Future Improvements

- Improve variable analysis by accounting for scope and reassignment.
- Expand the test dataset with more Python code examples.
- Compare results with established static-analysis tools.
- Add additional code-quality checks and a user-friendly interface.

## Author

Nimisha R.

## License

This project is available for educational and research purposes. A formal open-source license can be added if the project is intended for public reuse.
