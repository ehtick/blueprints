"""Formula 7.20 from NEN-EN 1992-1-1+C2:2011: Chapter 7 - Serviceability Limit State."""

from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011 import NEN_EN_1992_1_1_C2_2011
from blueprints.codes.formula import Formula
from blueprints.codes.latex_formula import LatexFormula, latex_replace_symbols
from blueprints.type_alias import DIMENSIONLESS, MPA
from blueprints.validations import raise_if_negative


class Form7Dot20EffectiveModulusCreep(Formula):
    r"""Class representing formula 7.20 for the calculation of [$E_{c,eff}$]."""

    label = "7.20"
    source_document = NEN_EN_1992_1_1_C2_2011

    def __init__(
        self,
        e_cm: MPA,
        phi_inf_t0: DIMENSIONLESS,
    ) -> None:
        r"""[$E_{c,eff}$] Calculation of the effective modulus of elasticity for concrete including creep.

        NEN-EN 1992-1-1+C2:2011 art.7.4.3(5) - Formula (7.20)

        Parameters
        ----------
        e_cm : MPA
            [$E_{cm}$] Secant modulus of elasticity of concrete [$MPa$].
        phi_inf_t0 : DIMENSIONLESS
            [$\phi(\infty, t_0)$] Creep coefficient relevant for the load and time interval (see 3.1.3) [$-$].
        """
        super().__init__()
        self.e_cm = e_cm
        self.phi_inf_t0 = phi_inf_t0

    @staticmethod
    def _evaluate(
        e_cm: MPA,
        phi_inf_t0: DIMENSIONLESS,
    ) -> MPA:
        """Evaluates the formula, for more information see the __init__ method."""
        raise_if_negative(e_cm=e_cm, phi_inf_t0=phi_inf_t0)

        return e_cm / (1 + phi_inf_t0)

    def latex(self) -> LatexFormula:
        """Returns LatexFormula object for formula 7.20."""
        _equation: str = r"\frac{E_{cm}}{1 + \phi(\infty , t_0)}"
        _numeric_equation: str = latex_replace_symbols(
            _equation,
            {
                r"E_{cm}": f"{self.e_cm:.3f}",
                r"\phi(\infty , t_0)": f"{self.phi_inf_t0:.3f}",
            },
            False,
        )
        return LatexFormula(
            return_symbol=r"E_{c,eff}",
            result=f"{self:.3f}",
            equation=_equation,
            numeric_equation=_numeric_equation,
            comparison_operator_label="=",
            unit="MPa",
        )
