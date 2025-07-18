"""Formula 6.3N from EN 1992-1-1:2004: Chapter 6 - Ultimate Limit State."""

from blueprints.codes.eurocode.en_1992_1_1_2004 import EN_1992_1_1_2004
from blueprints.codes.formula import Formula
from blueprints.codes.latex_formula import LatexFormula
from blueprints.type_alias import DIMENSIONLESS, MPA
from blueprints.validations import raise_if_negative


class Form6Dot3NShearCapacityWithoutRebar(Formula):
    r"""Class representing formula 6.3N for the calculation of the shear capacity without rebar, [$v_{min}$]."""

    label = "6.3N"
    source_document = EN_1992_1_1_2004

    def __init__(
        self,
        k: DIMENSIONLESS,
        f_ck: MPA,
    ) -> None:
        r"""[$v_{min}$] Shear capacity without rebar [$MPa$].

        EN 1992-1-1:2004 art.6.2.2(1) - Formula (6.3N)

        Parameters
        ----------
        k : DIMENSIONLESS
            [$k$] Factor which depends on the thickness concrete, see formula 6.2 [$-$].
        f_ck : MPA
            [$f_{ck}$] Characteristic compressive strength of concrete [$MPa$].
        """
        super().__init__()
        self.k = k
        self.f_ck = f_ck

    @staticmethod
    def _evaluate(
        k: DIMENSIONLESS,
        f_ck: MPA,
    ) -> MPA:
        """Evaluates the formula, for more information see the __init__ method."""
        raise_if_negative(k=k, f_ck=f_ck)

        return 0.035 * k**1.5 * f_ck**0.5

    def latex(self, n: int = 3) -> LatexFormula:
        """Returns LatexFormula object for formula 6.3N."""
        return LatexFormula(
            return_symbol=r"v_{min}",
            result=f"{self:.{n}f}",
            equation=r"0.035 \cdot k^{3/2} \cdot f_{ck}^{1/2}",
            numeric_equation=rf"0.035 \cdot {self.k:.{n}f}^{{3/2}} \cdot {self.f_ck:.{n}f}^{{1/2}}",
            comparison_operator_label="=",
            unit="MPa",
        )
