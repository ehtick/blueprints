"""Formula 7.5 from NEN-EN 1995-1-1+C1+A1:2011/C1:2012."""

import math

from blueprints.codes.eurocode.nen_en_1995_1_1_2011 import NEN_EN_1995_1_1_2011_2012
from blueprints.codes.formula import Formula
from blueprints.codes.latex_formula import LatexFormula, latex_replace_symbols
from blueprints.type_alias import HZ, KG_M2, NM2_M, M
from blueprints.validations import raise_if_less_or_equal_to_zero, raise_if_negative


class Form7Dot5NaturalFrequency(Formula):
    r"""Class representing formula 7.5 for the calculation of natural frequency [$f_{1}$]."""

    label = "7.5"
    source_document = NEN_EN_1995_1_1_2011_2012

    def __init__(self, length: M, ei_l: NM2_M, m: KG_M2) -> None:
        r"""[$f_{1}$] The natural frequency [$Hz$].

        NEN-EN 1995-1-1 art 7.3.3(4) - Formula (7.5)

        Parameters
        ----------
        length : M
            [$l$] Span of the floor [$m$].
        ei_l : NM2_M
            [$(EI)_{l}$] Equivalent plate bending stiffness of the floor around the axis perpendicular to the
            longitudinal axis of the beam [$Nm^{2}/m$].
        m : KG_M2
            [$m$] Mass per unit area [$kg/m^{2}$].

        Returns
        -------
        None
        """
        super().__init__()
        self.length = length
        self.ei_l = ei_l
        self.m = m

    @staticmethod
    def _evaluate(length: M, ei_l: NM2_M, m: KG_M2) -> HZ:
        """Evaluates the formula, for more information see the __init__ method."""
        raise_if_less_or_equal_to_zero(m=m, length=length)
        raise_if_negative(ei_l=ei_l)
        sqrt_ei_m = (ei_l / m) ** 0.5
        return (math.pi / (2 * length**2)) * sqrt_ei_m

    def latex(self) -> LatexFormula:
        """Returns LatexFormula object for formula 7.5."""
        eq1: str = r"\frac{\pi}{2 \cdot l^{2}} \cdot \sqrt{\frac{(EI)_{l}}{m}}"
        repl_symb = {"m": f"{self.m:.2f}", " l": f" {self.length:.2f}", "(EI)_{l}": f"{self.ei_l:.2f}"}
        return LatexFormula(
            return_symbol=r"f_{1}",
            result=f"{self:.2f}",
            equation=eq1,
            numeric_equation=latex_replace_symbols(eq1, repl_symb),
            comparison_operator_label="=",
        )
