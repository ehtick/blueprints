"""Formula 7.18 from NEN-EN 1992-1-1+C2:2011: Chapter 7 - Serviceability Limit State."""

from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011 import NEN_EN_1992_1_1_C2_2011
from blueprints.codes.formula import Formula
from blueprints.codes.latex_formula import LatexFormula, latex_replace_symbols
from blueprints.type_alias import DIMENSIONLESS
from blueprints.validations import raise_if_negative


class Form7Dot18DeformationParameter(Formula):
    r"""Class representing formula 7.18 for the calculation of [$\alpha$]."""

    label = "7.18"
    source_document = NEN_EN_1992_1_1_C2_2011

    def __init__(
        self,
        zeta: DIMENSIONLESS,
        alpha_l: DIMENSIONLESS,
        alpha_ll: DIMENSIONLESS,
    ) -> None:
        r"""[$\alpha$] Calculation of the deformation parameter [$\alpha$].

        NEN-EN 1992-1-1+C2:2011 art.7.4.3(3) - Formula (7.18)

        Parameters
        ----------
        zeta : DIMENSIONLESS
            [$\zeta$] Distribution coefficient allowing for tension stiffening at a section, calculated with Expression (7.19).
        alpha_l : DIMENSIONLESS
            [$\alpha_{I}$] Value of the parameter calculated for the uncracked condition
        alpha_ll : DIMENSIONLESS
            [$\alpha_{II}$] Value of the parameter calculated for the fully cracked condition.
        .
        """
        super().__init__()
        self.zeta = zeta
        self.alpha_l = alpha_l
        self.alpha_ll = alpha_ll

    @staticmethod
    def _evaluate(
        zeta: DIMENSIONLESS,
        alpha_l: DIMENSIONLESS,
        alpha_ll: DIMENSIONLESS,
    ) -> DIMENSIONLESS:
        """Evaluates the formula, for more information see the __init__ method."""
        raise_if_negative(alpha_ll=alpha_ll, alpha_l=alpha_l, zeta=zeta)

        return zeta * alpha_ll + (1 - zeta) * alpha_l

    def latex(self) -> LatexFormula:
        """Returns LatexFormula object for formula 7.18."""
        _equation: str = r"\zeta \cdot \alpha_{II} + (1 - \zeta) \cdot \alpha_{I}"
        _numeric_equation: str = latex_replace_symbols(
            _equation,
            {
                r"\zeta": f"{self.zeta:.3f}",
                r"\alpha_{II}": f"{self.alpha_ll:.3f}",
                r"\alpha_{I}": f"{self.alpha_l:.3f}",
            },
            False,
        )
        return LatexFormula(
            return_symbol=r"\alpha",
            result=f"{self:.3f}",
            equation=_equation,
            numeric_equation=_numeric_equation,
            comparison_operator_label="=",
            unit="-",
        )
