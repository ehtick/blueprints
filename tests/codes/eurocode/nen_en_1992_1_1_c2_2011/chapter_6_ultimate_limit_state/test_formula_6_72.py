"""Testing formula 6.72 of NEN-EN 1992-1-1+C2:2011."""

import pytest

from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011.chapter_6_ultimate_limit_state.formula_6_72 import (
    Form6Dot72FatigueResistanceConcreteCompression,
)
from blueprints.validations import NegativeValueError


class TestForm6Dot72FatigueResistanceConcreteCompression:
    """Validation for formula 6.72 from NEN-EN 1992-1-1+C2:2011."""

    def test_evaluation(self) -> None:
        """Tests the evaluation of the result."""
        # Example values
        e_cd_max_equ = 0.8
        r_equ = 0.5

        # Object to test
        formula = Form6Dot72FatigueResistanceConcreteCompression(e_cd_max_equ=e_cd_max_equ, r_equ=r_equ)

        # Expected result, manually calculated
        expected_result = False

        assert formula == expected_result

    @pytest.mark.parametrize(
        ("e_cd_max_equ", "r_equ"),
        [
            (-0.8, 0.5),  # e_cd_max_equ is negative
            (0.8, -0.5),  # r_equ is negative
        ],
    )
    def test_raise_error_when_invalid_values_are_given(self, e_cd_max_equ: float, r_equ: float) -> None:
        """Test invalid values."""
        with pytest.raises(NegativeValueError):
            Form6Dot72FatigueResistanceConcreteCompression(e_cd_max_equ=e_cd_max_equ, r_equ=r_equ)

    @pytest.mark.parametrize(
        ("representation", "expected"),
        [
            (
                "complete",
                r"CHECK \to E_{cd,max,equ} + 0.43 \cdot \sqrt{1 - R_{equ}} \leq 1 \to "
                r"0.800 + 0.43 \cdot \sqrt{1 - 0.500} \leq 1 \to \text{Not OK}",
            ),
            ("short", r"CHECK \to \text{Not OK}"),
        ],
    )
    def test_latex(self, representation: str, expected: str) -> None:
        """Test the latex representation of the formula."""
        # Example values
        e_cd_max_equ = 0.8
        r_equ = 0.5

        # Object to test
        latex = Form6Dot72FatigueResistanceConcreteCompression(e_cd_max_equ=e_cd_max_equ, r_equ=r_equ).latex()

        actual = {
            "complete": latex.complete,
            "short": latex.short,
        }

        assert expected == actual[representation], f"{representation} representation failed."
