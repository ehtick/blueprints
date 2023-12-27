"""Testing formula 8.18 of NEN-EN 1992-1-1+C2:2011."""
# pylint: disable=duplicate-code
import pytest

from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011.chapter_8_detailing_of_reinforcement_and_prestressing_tendons.formula_8_16 import (
    Form8Dot16BasicTransmissionLength,
)
from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011.chapter_8_detailing_of_reinforcement_and_prestressing_tendons.formula_8_18 import (
    Form8Dot18DesignValueTransmissionLength2,
)
from blueprints.validations import NegativeValueError


class TestForm8Dot18DesignValueTransmissionLength2:
    """Validation for formula 8.18 from NEN-EN 1992-1-1+C2:2011."""

    def test_evaluation(self) -> None:
        """Test the evaluation of the result."""
        # example values
        l_pt = 140  # mm
        form_8_18 = Form8Dot18DesignValueTransmissionLength2(l_pt=l_pt)
        # manually calculated result
        manually_calculated_result = 168  # mm

        assert form_8_18 == pytest.approx(expected=manually_calculated_result, rel=1e-4)

    def test_raise_error_if_negative_l_pt(self) -> None:
        """Test that a NegativeValueError is raised when a negative value is passed for l_pt."""
        l_pt = -1
        with pytest.raises(NegativeValueError):
            Form8Dot18DesignValueTransmissionLength2(l_pt=l_pt)

    def test_integration_with_form_8_dot_16(self) -> None:
        """Test integration between formula 8.16 and 8.17."""
        alpha_1 = 1  # [-]
        alpha_2 = 0.25  # [-]
        diameter = 8  # mm
        sigma_pm0 = 350  # MPa
        f_bpt = 5  # MPa
        l_pt = Form8Dot16BasicTransmissionLength(
            alpha_1=alpha_1,
            alpha_2=alpha_2,
            diameter=diameter,
            sigma_pm0=sigma_pm0,
            f_bpt=f_bpt,
        )

        form_8_17 = Form8Dot18DesignValueTransmissionLength2(l_pt=l_pt)
        manually_calculated_result = 168  # mm

        assert form_8_17 == pytest.approx(expected=manually_calculated_result, rel=1e-4)
