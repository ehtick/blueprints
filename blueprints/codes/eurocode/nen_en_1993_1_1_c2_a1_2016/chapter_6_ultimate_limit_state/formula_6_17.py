"""Formula 6.17 from NEN-EN 1993-1-1+C2+A1:2016: Chapter 6 - Ultimate Limit State."""

from blueprints.codes.eurocode.nen_en_1993_1_1_c2_a1_2016 import NEN_EN_1993_1_1_C2_A1_2016
from blueprints.codes.formula import Formula
from blueprints.codes.latex_formula import LatexFormula, latex_replace_symbols
from blueprints.type_alias import N
from blueprints.validations import raise_if_less_or_equal_to_zero, raise_if_negative


class Form6Dot17CheckShearForce(Formula):
    r"""Class representing formula 6.17 for checking the design value of the shear force."""

    label = "6.17"
    source_document = NEN_EN_1993_1_1_C2_A1_2016

    def __init__(
        self,
        v_ed: N,
        v_c_rd: N,
    ) -> None:
        r"""Check the design value of the shear force at each cross section.

        NEN-EN 1993-1-1+C2+A1:2016 art.6.2.6(1) - Formula (6.17)

        Parameters
        ----------
        v_ed : N
            [$V_{Ed}$] Design value of the shear force [$N$].
        v_c_rd : N
            [$V_{c,Rd}$] Design shear resistance [$N$].
        """
        super().__init__()
        self.v_ed = v_ed
        self.v_c_rd = v_c_rd

    @staticmethod
    def _evaluate(
        v_ed: N,
        v_c_rd: N,
    ) -> bool:
        """Evaluates the formula, for more information see the __init__ method."""
        raise_if_less_or_equal_to_zero(v_c_rd=v_c_rd)
        raise_if_negative(v_ed=v_ed)

        return v_ed / v_c_rd <= 1.0

    def latex(self) -> LatexFormula:
        """Returns LatexFormula object for formula 6.17."""
        _equation: str = r"\left( \frac{V_{Ed}}{V_{c,Rd}} \leq 1.0 \right)"
        _numeric_equation: str = latex_replace_symbols(
            _equation,
            {
                "V_{Ed}": f"{self.v_ed:.3f}",
                "V_{c,Rd}": f"{self.v_c_rd:.3f}",
            },
            False,
        )
        return LatexFormula(
            return_symbol=r"CHECK",
            result="OK" if self.__bool__() else "\\text{Not OK}",
            equation=_equation,
            numeric_equation=_numeric_equation,
            comparison_operator_label="\\to",
            unit="",
        )
