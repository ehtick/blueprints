"""Formula 5.4 from EN 1992-1-1:2004: Chapter 5 - Structural Analysis."""

from blueprints.codes.eurocode.en_1992_1_1_2004 import EN_1992_1_1_2004
from blueprints.codes.formula import Formula
from blueprints.codes.latex_formula import LatexFormula
from blueprints.type_alias import DIMENSIONLESS, KN
from blueprints.validations import raise_if_negative


class Form5Dot4TransverseForceEffectBracingSystem(Formula):
    """Class representing formula 5.4 for the calculation of the effect of the inclination on bracing systems, [$H_{i}$].

    See Figure 5.1 b.
    """

    label = "5.4"
    source_document = EN_1992_1_1_2004

    def __init__(
        self,
        theta_i: DIMENSIONLESS,
        n_a: KN,
        n_b: KN,
    ) -> None:
        r"""[$H_{i}$] Effect of the inclination on bracing systems [$kN$].

        EN 1992-1-1:2004 art.5.2(8) - Formula (5.4)

        Parameters
        ----------
        theta_i : DIMENSIONLESS
            [$Θ_{i}$] Eccentricity, initial inclination imperfections [-].
        n_a : KN
            [$N_{a}$] Axial force in the member [$kN$].
        n_b : KN
            [$N_{b}$] Axial force in the member [$kN$].

        Notes
        -----
        where [$N_{a}$] and [$N_{b}$] are longitudinal forces contributing to [$H_{i}$].
        Positive values for compression, tension is not allowed.
        """
        super().__init__()
        self.theta_i = theta_i
        self.n_a = n_a
        self.n_b = n_b

    @staticmethod
    def _evaluate(
        theta_i: DIMENSIONLESS,
        n_a: KN,
        n_b: KN,
    ) -> KN:
        """Evaluates the formula, for more information see the __init__ method."""
        raise_if_negative(
            theta_i=theta_i,
            n_a=n_a,
            n_b=n_b,
        )
        return theta_i * (n_b - n_a)

    def latex(self, n: int = 3) -> LatexFormula:
        """Returns LatexFormula object for formula 5.4."""
        return LatexFormula(
            return_symbol=r"H_{i}",
            result=f"{self:.{n}f}",
            equation=r"Θ_{i} \cdot (N_{b} - N_{a})",
            numeric_equation=rf"{self.theta_i:.{n}f} \cdot ({self.n_b:.{n}f} - {self.n_a:.{n}f})",
            comparison_operator_label="=",
        )
