""" "Testing Formula 2.1b from NEN 9997-1+C2:2017: Chapter 2: Basis of geotechnical design."""

import pytest

from blueprints.codes.eurocode.nen_9997_1_c2_2017.chapter_2_basic_of_geotechnical_design.formula_2_1_b import Form2Dot1BRepresentativeValue
from blueprints.validations import NegativeValueError


class TestForm2Dot1BRepresentativeValue:
    """Validation for formula 2.1b from NEN 9997-1+C2:2017."""

    def test_evaluation(self) -> None:
        """Test the evaluation of the result."""
        # example values
        psi = 1.2  # [-]
        f_k = 100  # kN

        form_2_1_b = Form2Dot1BRepresentativeValue(psi=psi, f_k=f_k)

        # manually calculated result
        manually_calculated_result = 120

        assert form_2_1_b == pytest.approx(expected=manually_calculated_result, rel=1e-9)

    def test_raise_error_if_negative_psi(self) -> None:
        """Test that a NegativeValueError is raised when a negative value is passed for psi."""
        psi = -1
        f_k = 100

        with pytest.raises(NegativeValueError):
            Form2Dot1BRepresentativeValue(psi=psi, f_k=f_k)
