"""Formula 3.18 from EN 1992-1-1:2004: Chapter 3 - Materials."""

from blueprints.codes.eurocode.en_1992_1_1_2004 import EN_1992_1_1_2004
from blueprints.codes.formula import Formula
from blueprints.codes.latex_formula import LatexFormula
from blueprints.type_alias import MPA


class Form3Dot18CompressiveStressConcrete(Formula):
    """Class representing formula 3.18 for the calculation of compressive stress in concrete using stress-strain diagram of figure 3.3."""

    label = "3.18"
    source_document = EN_1992_1_1_2004

    def __init__(
        self,
        f_cd: MPA,
    ) -> None:
        r"""[$\sigma_c$] Compressive stress in concrete using stress-strain diagram of figure 3.3 [$MPa$].

        EN 1992-1-1:2004 art.3.1.7(1) - Formula (3.18)

        Parameters
        ----------
        f_cd : MPA
            [$f_{cd}$] Design value compressive strength concrete [$MPa$].

        Returns
        -------
        None
        """
        super().__init__()
        self.f_cd = f_cd

    @staticmethod
    def _evaluate(
        f_cd: MPA,
    ) -> MPA:
        """Evaluates the formula, for more information see the __init__ method."""
        if f_cd < 0:
            raise ValueError(f"Invalid f_cd: {f_cd}. f_cd cannot be negative")
        return f_cd

    def latex(self, n: int = 3) -> LatexFormula:
        """Returns LatexFormula object for formula 3.18."""
        return LatexFormula(
            return_symbol=r"\sigma_c",
            result=f"{self:.{n}f}",
            equation=r"f_{cd}",
            numeric_equation=rf"{self.f_cd:.{n}f}",
            comparison_operator_label="=",
        )
