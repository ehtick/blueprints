"""Formula 5.3b from EN 1992-1-1:2004: Chapter 5 - Structural Analysis."""

from blueprints.codes.eurocode.en_1992_1_1_2004 import EN_1992_1_1_2004
from blueprints.codes.formula import Formula
from blueprints.codes.latex_formula import LatexFormula
from blueprints.type_alias import DIMENSIONLESS, KN
from blueprints.validations import raise_if_negative


class Form5Dot3bTransverseForceBracedMembers(Formula):
    """Class representing formula 5.3b for the calculation of the transverse force for braced members, [$H_{i}$].

    See Figure 5.1 a2.
    """

    label = "5.3b"
    source_document = EN_1992_1_1_2004

    def __init__(
        self,
        theta_i: DIMENSIONLESS,
        n_axial_force: KN,
    ) -> None:
        r"""[$H_{i}$] Transverse force for braced members [$kN$].

        EN 1992-1-1:2004 art.5.2(7) - Formula (5.3b)

        Parameters
        ----------
        theta_i : DIMENSIONLESS
            [$Θ_{i}$] Eccentricity, initial inclination imperfections [-].

            Use your own implementation of this value or use the :class:`Form5Dot1Imperfections` class.
        n_axial_force : KN
            [$N$] Axial force [$kN$].

            Positive values for compression, tension is not allowed.

        Notes
        -----
        Eccentricity is suitable for statically determinate members, whereas transverse load can be used for
        both determinate and indeterminate members. The force [$H_{i}$] may be substituted by some other equivalent
        transverse action.
        """
        super().__init__()
        self.theta_i = theta_i
        self.n_axial_force = n_axial_force

    @staticmethod
    def _evaluate(
        theta_i: DIMENSIONLESS,
        n_axial_force: KN,
    ) -> KN:
        """Evaluates the formula, for more information see the __init__ method."""
        raise_if_negative(theta_i=theta_i, n_axial_force=n_axial_force)
        return 2 * theta_i * n_axial_force

    def latex(self, n: int = 3) -> LatexFormula:
        """Returns LatexFormula object for formula 5.3b."""
        return LatexFormula(
            return_symbol=r"H_{i}",
            result=f"{self:.{n}f}",
            equation=r"2\theta_{i}N",
            numeric_equation=rf"2\cdot{self.theta_i:.{n}f}\cdot{self.n_axial_force:.{n}f}",
            comparison_operator_label="=",
        )
