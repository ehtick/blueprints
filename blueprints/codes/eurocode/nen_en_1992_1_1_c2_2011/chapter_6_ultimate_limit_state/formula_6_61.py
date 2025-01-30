"""Formula 6.61 from NEN-EN 1992-1-1+C2:2011: Chapter 6 - Ultimate Limit State."""

from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011 import NEN_EN_1992_1_1_C2_2011
from blueprints.codes.formula import Formula
from blueprints.codes.latex_formula import LatexFormula, latex_replace_symbols
from blueprints.type_alias import DIMENSIONLESS, MPA
from blueprints.validations import raise_if_negative


class Form6Dot61DesignValueCompressiveStressResistance(Formula):
    r"""Class representing formula 6.61 for the calculation of :math:`\sigma_{Rd,max}`."""

    label = "6.61"
    source_document = NEN_EN_1992_1_1_C2_2011

    def __init__(
        self,
        k_2: DIMENSIONLESS,
        nu_prime: DIMENSIONLESS,
        f_cd: MPA,
    ) -> None:
        r""":math:`\sigma_{Rd,max}` Calculation of :math:`\sigma_{Rd,max}`.

        NEN-EN 1992-1-1+C2:2011 art.6.5.4(4) - Formula (6.61)

        Parameters
        ----------
        k_2 : float
            :math:`k_2` Coefficient for the design value of compressive stress resistance [-].
            Note: The value of :math:`k_2` for use in a Country may be found in its National Annex.
            The recommended value is 0.85.
        nu_prime : float
            :math:`\nu'` Reduction factor for the design value of compressive stress resistance [-].
        f_cd : float
            :math:`f_{cd}` Design value of compressive strength [MPa].
        """
        super().__init__()
        self.k_2 = k_2
        self.nu_prime = nu_prime
        self.f_cd = f_cd

    @staticmethod
    def _evaluate(
        k_2: DIMENSIONLESS,
        nu_prime: DIMENSIONLESS,
        f_cd: MPA,
    ) -> MPA:
        """Evaluates the formula, for more information see the __init__ method."""
        raise_if_negative(k_2=k_2, nu_prime=nu_prime, f_cd=f_cd)

        return k_2 * nu_prime * f_cd

    def latex(self) -> LatexFormula:
        """Returns LatexFormula object for formula 6.61."""
        _equation: str = r"k_2 \cdot \nu' \cdot f_{cd}"
        _numeric_equation: str = latex_replace_symbols(
            _equation,
            {
                r"k_2": f"{self.k_2:.3f}",
                r"\nu'": f"{self.nu_prime:.3f}",
                r"f_{cd}": f"{self.f_cd:.3f}",
            },
            False,
        )
        return LatexFormula(
            return_symbol=r"\sigma_{Rd,max}",
            result=f"{self:.3f}",
            equation=_equation,
            numeric_equation=_numeric_equation,
            comparison_operator_label="=",
            unit="MPa",
        )
