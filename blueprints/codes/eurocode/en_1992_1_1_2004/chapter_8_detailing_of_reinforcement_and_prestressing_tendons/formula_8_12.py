"""Formula 8.12 from EN 1992-1-1:2004: Chapter 8: Detailing of reinforcement and prestressing tendons."""

from blueprints.codes.eurocode.en_1992_1_1_2004 import EN_1992_1_1_2004
from blueprints.codes.formula import Formula
from blueprints.codes.latex_formula import LatexFormula
from blueprints.type_alias import DIMENSIONLESS, MM2
from blueprints.validations import raise_if_negative


class Form8Dot12AdditionalShearReinforcement(Formula):
    """Class representing formula 8.12 for the calculation of the minimum additional shear reinforcement in the anchorage zones where transverse
    compression is not present for straight anchorage lengths, in the direction parallel to the tension face.
    """

    label = "8.12"
    source_document = EN_1992_1_1_2004

    def __init__(
        self,
        a_s: MM2,
        n_1: DIMENSIONLESS,
    ) -> None:
        r"""[$A_{sh}$] Minimum additional shear reinforcement in the anchorage zones where transverse compression is not present for straight
        anchorage lengths, in the direction parallel to the tension face [$mm^2$].

        EN 1992-1-1:2004 art.8.8(6) - Formula (8.12)

        Parameters
        ----------
        a_s: MM2
            [$A_{s}$] Cross sectional area of reinforcement [$mm²$].
        n_1: DIMENSIONLESS
            [$n_{1}$] Number of layers with bars anchored at the same point in the member [$-$].
        """
        super().__init__()
        self.a_s = a_s
        self.n_1 = n_1

    @staticmethod
    def _evaluate(
        a_s: MM2,
        n_1: DIMENSIONLESS,
    ) -> MM2:
        """Evaluates the formula, for more information see the __init__ method."""
        raise_if_negative(a_s=a_s, n_1=n_1)
        return 0.25 * a_s * n_1

    def latex(self, n: int = 2) -> LatexFormula:
        """Returns LatexFormula object for formula 8.12."""
        return LatexFormula(
            return_symbol=r"A_{sh}",
            result=f"{self:.{n}f}",
            equation=r"0.25 \cdot A_s \cdot n_1",
            numeric_equation=rf"0.25 \cdot {self.a_s:.{n}f} \cdot {self.n_1:.{n}f}",
            comparison_operator_label="=",
        )
