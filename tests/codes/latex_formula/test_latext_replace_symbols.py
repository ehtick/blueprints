import pytest

from blueprints.codes.latex_formula import latex_replace_symbols


# Success tests using pytest
@pytest.mark.parametrize("latex_template, replacements, unique_check, expected", [
    (r"\frac{A}{B}", {'A': 'x', 'B': 'y'}, True, r"\frac{x}{y}"),
    (r"\frac{A}{B}", {'A': 'x', 'B': 'y'}, False, r"\frac{x}{y}"),
    (r"\frac{A}{B}", {'A': 'x', 'B': 'y'}, False, r"\frac{x}{y}"),
    (r"\frac{A}{B}", {'A': 'x', 'B': 'y'}, False, r"\frac{x}{y}"),
    (
        r"\frac{k_{mod}}{\gamma_{R}}", 
        {'k_{mod}': '0.9', r'\gamma_{R}': '1.2'},
        False,
        r"\frac{0.9}{1.2}", 
    ),
])
def test_latex_replace_symbols_success(latex_template, replacements, unique_check, expected):
    """Test successful symbol replacements in LaTeX strings."""
    result = latex_replace_symbols(latex_template, replacements, unique_check)
    assert result == expected

# Error tests using pytest
@pytest.mark.parametrize("latex_template, replacements, unique_check, expected_exception", [
    (r"\frac{A}{B}", {'C': 'x'}, True, "Symbol 'C' not found in the template."),
    (r"\frac{A}{A}", {'A': 'x'}, True, "Symbol 'A' found multiple times in the template."),
])
def test_latex_replace_symbols_error(
    latex_template,
    replacements,
    unique_check,
    expected_exception
):
    """Test error conditions when replacing symbols in LaTeX strings."""
    with pytest.raises(ValueError, match=expected_exception):
        latex_replace_symbols(latex_template, replacements, unique_check)