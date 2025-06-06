"""Formula 4.2 from NEN-EN 1993-1-8+C2:2011: Chapter 4 - Welded Connections."""

from blueprints.codes.eurocode.nen_en_1993_1_8_c2_2011 import NEN_EN_1993_1_8_C2_2011
from blueprints.codes.formula import Formula
from blueprints.codes.latex_formula import LatexFormula, latex_replace_symbols
from blueprints.type_alias import N
from blueprints.validations import raise_if_negative


class Form4Dot2CheckWeldedConnection(Formula):
    r"""Class representing formula 4.2 for checking welded connections."""

    label = "4.2"
    source_document = NEN_EN_1993_1_8_C2_2011

    def __init__(
        self,
        fw_ed: N,
        fw_rd: N,
    ) -> None:
        r"""Check the force in the weld per unit length against its resistance.

        NEN-EN 1993-1-8+C2:2011 art.4.5.3.3(1) - Formula (4.2)

        Parameters
        ----------
        fw_ed : N
            [$F_{w,Ed}$] Design value of the force in the weld per unit length [$N$].
        fw_rd : N
            [$F_{w,Rd}$] Design value of the resistance of the weld per unit length [$N$].
        """
        super().__init__()
        self.fw_ed = fw_ed
        self.fw_rd = fw_rd

    @staticmethod
    def _evaluate(
        fw_ed: N,
        fw_rd: N,
    ) -> bool:
        """Evaluates the formula, for more information see the __init__ method."""
        raise_if_negative(fw_ed=fw_ed, fw_rd=fw_rd)

        return fw_ed <= fw_rd

    def latex(self) -> LatexFormula:
        """Returns LatexFormula object for formula 4.2."""
        _equation: str = r"F_{w,Ed} \leq F_{w,Rd}"
        _numeric_equation: str = latex_replace_symbols(
            _equation,
            {
                "F_{w,Ed}": f"{self.fw_ed:.3f}",
                "F_{w,Rd}": f"{self.fw_rd:.3f}",
            },
            False,
        )
        _numeric_equation_with_units: str = latex_replace_symbols(
            _equation,
            {
                "F_{w,Ed}": rf"{self.fw_ed:.3f} \ N",
                "F_{w,Rd}": rf"{self.fw_rd:.3f} \ N",
            },
            False,
        )
        return LatexFormula(
            return_symbol=r"CHECK",
            result="OK" if self.__bool__() else "\\text{Not OK}",
            equation=_equation,
            numeric_equation=_numeric_equation,
            numeric_equation_with_units=_numeric_equation_with_units,
            comparison_operator_label="\\to",
            unit="",
        )
