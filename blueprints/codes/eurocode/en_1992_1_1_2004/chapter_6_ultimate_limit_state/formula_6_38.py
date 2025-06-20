"""Formula 6.38 from EN 1992-1-1:2004: Chapter 6 - Ultimate limit state."""

from blueprints.codes.eurocode.en_1992_1_1_2004 import EN_1992_1_1_2004
from blueprints.codes.formula import Formula
from blueprints.codes.latex_formula import LatexFormula
from blueprints.type_alias import DIMENSIONLESS, MM, MPA, N
from blueprints.validations import raise_if_less_or_equal_to_zero, raise_if_negative


class Form6Dot38MaxShearStress(Formula):
    r"""Class representing formula 6.38 for the calculation of the maximum shear stress, [$v_{Ed}$]."""

    label = "6.38"
    source_document = EN_1992_1_1_2004

    def __init__(
        self,
        beta: DIMENSIONLESS,
        v_ed: N,
        u_i: MM,
        d: MM,
    ) -> None:
        r"""[$v_{Ed}$] Maximum shear stress [$MPa$].

        EN 1992-1-1:2004 art.6.4.3(3) - Formula (6.38)

        Parameters
        ----------
        beta : DIMENSIONLESS
            [$\beta$] Factor which depends on the distribution of the support reaction, see equation 6.39.
        v_ed : N
            [$V_{Ed}$] Design value of the shear force [$N$].
        u_i : MM
            [$u_{i}$] Length of the control perimeter being considered [$mm$].
        d : MM
            [$d$] Mean effective depth of the slab, which may be taken as (dy + dz)/2 [$mm$].
        """
        super().__init__()
        self.beta = beta
        self.v_ed = v_ed
        self.u_i = u_i
        self.d = d

    @staticmethod
    def _evaluate(
        beta: DIMENSIONLESS,
        v_ed: N,
        u_i: MM,
        d: MM,
    ) -> MPA:
        """Evaluates the formula, for more information see the __init__ method."""
        raise_if_negative(
            beta=beta,
            v_ed=v_ed,
        )
        raise_if_less_or_equal_to_zero(u_i=u_i, d=d)

        return beta * v_ed / (u_i * d)

    def latex(self, n: int = 3) -> LatexFormula:
        """Returns LatexFormula object for formula 6.38."""
        return LatexFormula(
            return_symbol=r"v_{Ed}",
            result=f"{self:.{n}f}",
            equation=r"\beta \cdot \frac{V_{Ed}}{u_{i} \cdot d}",
            numeric_equation=rf"{self.beta:.{n}f} \cdot \frac{{{self.v_ed:.{n}f}}}{{{self.u_i:.{n}f} \cdot {self.d:.{n}f}}}",
            comparison_operator_label="=",
            unit="MPa",
        )
