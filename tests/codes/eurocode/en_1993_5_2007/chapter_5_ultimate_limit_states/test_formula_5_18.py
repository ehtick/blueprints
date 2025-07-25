"""Testing formula 5.18 of EN 1993-5:2007."""

import pytest

from blueprints.codes.eurocode.en_1993_5_2007.chapter_5_ultimate_limit_states.formula_5_18 import Form5Dot18CompressionCheckUProfilesClass1And2
from blueprints.validations import LessOrEqualToZeroError, NegativeValueError


class TestForm5Dot18CompressionCheckUProfilesClass1And2:
    """Validation for formula 5.18 from EN 1993-5:2007."""

    def test_evaluation(self) -> None:
        """Tests the evaluation of the result."""
        # Example values
        n_ed = 10.0  # kN
        n_pl_rd = 120.0  # kN

        # Object to test
        formula = Form5Dot18CompressionCheckUProfilesClass1And2(
            n_ed=n_ed,
            n_pl_rd=n_pl_rd,
        )

        # Expected result, manually calculated
        expected_result = True

        assert formula == expected_result
        assert formula.unity_check == n_ed / n_pl_rd

    @pytest.mark.parametrize(
        ("n_ed", "n_pl_rd"),
        [
            (10.0, 0.0),  # n_pl_rd zero
            (10.0, -120.0),  # n_pl_rd negative
        ],
    )
    def test_raise_error_when_invalid_values_are_given(self, n_ed: float, n_pl_rd: float) -> None:
        """Test invalid values."""
        with pytest.raises((NegativeValueError, LessOrEqualToZeroError)):
            Form5Dot18CompressionCheckUProfilesClass1And2(n_ed=n_ed, n_pl_rd=n_pl_rd)

    @pytest.mark.parametrize(
        ("representation", "expected"),
        [
            (
                "complete",
                r"CHECK \to \frac{N_{Ed}}{N_{pl,Rd}} \leq 0.25 \to \frac{10.000}{120.000} \leq 0.25 \to OK",
            ),
            ("short", r"CHECK \to OK"),
        ],
    )
    def test_latex(self, representation: str, expected: str) -> None:
        """Test the latex representation of the formula."""
        # Example values
        n_ed = 10.0  # kN
        n_pl_rd = 120.0  # kN

        # Object to test
        latex = Form5Dot18CompressionCheckUProfilesClass1And2(n_ed=n_ed, n_pl_rd=n_pl_rd).latex()

        actual = {
            "complete": latex.complete,
            "short": latex.short,
        }

        assert expected == actual[representation], f"{representation} representation failed."
