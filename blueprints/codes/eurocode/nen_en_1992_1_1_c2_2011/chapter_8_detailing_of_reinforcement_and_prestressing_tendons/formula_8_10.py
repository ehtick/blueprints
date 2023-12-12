"""Formula 8.10 from NEN-EN 1992-1-1+C2:2011: Chapter 8: Detailing of reinforcement and prestressing tendons"""
# pylint: disable=arguments-differ
from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011 import NEN_EN_1992_1_1_C2_2011
from blueprints.codes.formula import Formula
from blueprints.type_alias import DIMENSIONLESS, MM
from blueprints.validations import raise_if_negative


class Form8Dot10DesignLapLength(Formula):
    """Class representing formula 8.10 for the calculation of the design lap length l0 [mm]."""

    label = "8.10"
    source_document = NEN_EN_1992_1_1_C2_2011

    def __init__(
        self,
        alpha_1: DIMENSIONLESS,
        alpha_2: DIMENSIONLESS,
        alpha_3: DIMENSIONLESS,
        alpha_5: DIMENSIONLESS,
        alpha_6: DIMENSIONLESS,
        l_b_rqd: MM,
        l_0_min: MM,
    ) -> None:
        """[l0] Design lap length [mm].

        NEN-EN 1992-1-1+C2:2011 art.8.4.4(1) - Formula (8.4)

        Parameters
        ----------
        alpha_1 : DIMENSIONLESS
            [α1] Coefficient for the effect of the form of the bars assuming adequate cover (see figure 8.1) [-].
            = 1.0 for bars in compression.
            = 1.0 for straight bars in tension.
            = 1.0 if cd <= 3 * Φ for bars other than straight in tension (see figure 8.1 (b), (c) and (d)).
            = 0.7 if cd > 3 * Φ for bars other than straight in tension (see figure 8.1 (b), (c) and (d)).
            Note: see figure 8.3 for values of cd.
        alpha_2 : DIMENSIONLESS
            [α2] Coefficient for the effect of minimum concrete cover (see figure 8.3) [-].
            = 1.0 for bars in compression.
            = 1 - 0.15 * (cd - Φ) / Φ <= 1 with a minimum of 0.7 for straight bars in tension.
            = 1 - 0.15 * (cd - 3 * Φ) / Φ <= 1 with a minimum of 0.7 for bars other than straight in tension (see figure 8.1 (b), (c) and (d)).
            Note: see figure 8.3 for values of cd.
        alpha_3 : DIMENSIONLESS
            [α3] Coefficient for the effect of confinement by transverse reinforcement [-].
            = 1.0 for bars in compression.
            = 1 - K * λ <= 1 with a minimum of 0.7 for bars in tension.
            Where: λ = (ΣAst - ΣAst,min) / As.
            Where: ΣAst,min = As * (σsd/fyd)
            With As = area of one lapped bar [mm²].
            Note: see figure 8.4 for values of K, As and Ast.
        alpha_5 : DIMENSIONLESS
            [α5] Coefficient for the effect of the pressure transverse to the plane of splitting along the design anchorage length lbd (see 8.6) [-].
            = 1 - 0.04 * p <= 1 with a minimum of 0.7 for all types of anchorage in compression.
            Where: p = transverse pressure at ultimate limit state along lbd [MPa].
        alpha_6 : DIMENSIONLESS
            [α6] Coefficient for the effect of reinforcement ratio [-].
            = (ρl/25)^0.5 <= 1.5 with a minimum of 1.0.
            Where: ρl = reinforcement percentage lapped within 0,65 l0 from the centre of the lap length considered (see figure 8.8) [-].
        l_b_rqd : MM
            [lbrqd] Required anchorage length from formula 8.3 [mm].
            = (Φ/4) * (σsd/fbd)
            Use your own implementation of this formula or use the Form8Dot3RequiredAnchorageLength class.
        l_0_min : MM
            [l0min] Minimum design lap length [mm].
            = max(0.3 * alpha_6 * l_b_rqd, 15 * Φ, 200) (formula 8.11).
            Use your own implementation of this formula or use Form8Dot11MinimumDesignLapLength class.
        """
        super().__init__()
        self.alpha_1 = alpha_1
        self.alpha_2 = alpha_2
        self.alpha_3 = alpha_3
        self.alpha_5 = alpha_5
        self.alpha_6 = alpha_6
        self.l_b_rqd = l_b_rqd
        self.l_0_min = l_0_min

    @staticmethod
    def _evaluate(
        alpha_1: DIMENSIONLESS,
        alpha_2: DIMENSIONLESS,
        alpha_3: DIMENSIONLESS,
        alpha_5: DIMENSIONLESS,
        alpha_6: DIMENSIONLESS,
        l_b_rqd: MM,
        l_0_min: MM,
    ) -> MM:
        """Evaluates the formula, for more information see the __init__ method"""
        raise_if_negative(
            alpha_1=alpha_1,
            alpha_2=alpha_2,
            alpha_3=alpha_3,
            alpha_5=alpha_5,
            alpha_6=alpha_6,
            l_b_rqd=l_b_rqd,
            l_0_min=l_0_min,
        )
        return max(alpha_1 * alpha_2 * alpha_3 * alpha_5 * alpha_6 * l_b_rqd, l_0_min)
