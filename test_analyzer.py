
import unittest

from analyzer import analyze_code


class TestAnalyzer(unittest.TestCase):
    """Tests for the Python code analyzer."""

    def test_valid_code(self):
        code = "x = 10\nprint(x)"
        self.assertEqual(analyze_code(code), [])

    def test_syntax_error(self):
        code = "if True print('hello')"
        issues = analyze_code(code)

        self.assertTrue(
            any(issue["severity"] == "critical" for issue in issues)
        )

    def test_missing_docstring(self):
        code = "def greet():\n    print('Hello')"
        issues = analyze_code(code)

        self.assertTrue(
            any(
                "no documentation" in issue["message"]
                for issue in issues
            )
        )

    def test_unused_variable(self):
        code = "unused_value = 10"
        issues = analyze_code(code)

        self.assertTrue(
            any(
                "unused_value" in issue["message"]
                for issue in issues
            )
        )


if __name__ == "__main__":
    unittest.main()
