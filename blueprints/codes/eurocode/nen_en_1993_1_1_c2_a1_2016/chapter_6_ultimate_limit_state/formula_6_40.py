"""Formula 6.40 from NEN-EN 1993-1-1+C2+A1:2016: Chapter 6 - Ultimate Limit State."""

from blueprints.codes.eurocode.nen_en_1993_1_1_c2_a1_2016 import NEN_EN_1993_1_1_C2_A1_2016
from blueprints.codes.formula import Formula
from blueprints.codes.latex_formula import LatexFormula, latex_replace_symbols
from blueprints.type_alias import DIMENSIONLESS, NMM
from blueprints.validations import raise_if_less_or_equal_to_zero, raise_if_negative


class Form6Dot40ReducedBendingMomentResistance(Formula):
    r"""Class representing formula 6.40 for the calculation of [$M_{N,z,Rd}$]."""

    label = "6.40"
    source_document = NEN_EN_1993_1_1_C2_A1_2016

    def __init__(
        self,
        mpl_z_rd: NMM,
        n: DIMENSIONLESS,
        a_f: DIMENSIONLESS,
    ) -> None:
        r"""[$M_{N,z,Rd}$] Calculation of the reduced bending moment [$Nmm$].

        NEN-EN 1993-1-1+C2+A1:2016 art.6.2.9.1(5) - Formula (6.40)

        Parameters
        ----------
        mpl_z_rd : NMM
            [$M_{pl,z,Rd}$] Plastic bending moment resistance about the z-axis [$Nmm$].
        n : DIMENSIONLESS
            [$n$] Axial force ratio, see equation 6.38n (dimensionless).
        a_f : DIMENSIONLESS
            [$a_f$] Reduction factor for the flange (dimensionless).
        """
        super().__init__()
        self.mpl_z_rd = mpl_z_rd
        self.n = n
        self.a_f = a_f

    @staticmethod
    def _evaluate(
        mpl_z_rd: NMM,
        n: DIMENSIONLESS,
        a_f: DIMENSIONLESS,
    ) -> NMM:
        """Evaluates the formula, for more information see the __init__ method."""
        raise_if_negative(mpl_z_rd=mpl_z_rd, n=n, a_f=a_f)
        raise_if_less_or_equal_to_zero(denominator=(1 - 0.5 * a_f))

        return min(mpl_z_rd * (1 - n) / (1 - 0.5 * a_f), mpl_z_rd)

    def latex(self) -> LatexFormula:
        """Returns LatexFormula object for formula 6.40."""
        _equation: str = r"\min \left( M_{pl,z,Rd} \cdot \frac{1 - n}{1 - 0.5 \cdot a_f}, M_{pl,z,Rd} \right)"
        _numeric_equation: str = latex_replace_symbols(
            _equation,
            {
                r"M_{pl,z,Rd}": f"{self.mpl_z_rd:.3f}",
                r" n": f" {self.n:.3f}",
                r"a_f": f"{self.a_f:.3f}",
            },
            False,
        )
        _numeric_equation_with_units: str = latex_replace_symbols(
            _equation,
            {
                r"M_{pl,z,Rd}": rf"{self.mpl_z_rd:.3f} \ Nmm",
                r" n": rf" {self.n:.3f}",
                r"a_f": rf"{self.a_f:.3f}",
            },
            False,
        )
        return LatexFormula(
            return_symbol=r"M_{N,z,Rd}",
            result=f"{self:.3f}",
            equation=_equation,
            numeric_equation=_numeric_equation,
            numeric_equation_with_units=_numeric_equation_with_units,
            comparison_operator_label=r"=",
            unit="Nmm",
        )
