"""Formula 9.3 from EN 1992-1-1:2004: Chapter 9 - Detailing of members and particular rules."""

from blueprints.codes.eurocode.en_1992_1_1_2004 import EN_1992_1_1_2004
from blueprints.codes.formula import Formula
from blueprints.codes.latex_formula import LatexFormula
from blueprints.type_alias import KN, MM
from blueprints.validations import raise_if_negative


class Form9Dot3ShiftInMomentDiagram(Formula):
    """Class representing the formula 9.3 for the calculation of anchorage length of bottom reinforcement at an end support using the shift rule."""

    label = "9.3"
    source_document = EN_1992_1_1_2004

    def __init__(
        self,
        v_ed: KN,
        a_l: MM,
        z: MM,
        n_ed: KN,
    ) -> None:
        r"""[$F_{Ed}$] Force to be anchored according to the shift rule [$kN$].

        EN 1992-1-1:2004 art.9.2.1.4(2) - Formula (9.3)

        Parameters
        ----------
        v_ed: KN
            [$V_{Ed}$] Design value shear force [$kN$].
        a_l: MM
            [$a_l$] Shift in the moment diagram of an element with shear reinforcement based on art. 9.2.1.3 (2) [$mm$].
            Use your own implementation of this value or use the Form9Dot2ShiftInMomentDiagram class.
        z: MM
            [$z$] The internal lever arm for an element with constant height, corresponding to the bending moment in the considered element. In the
            shear force calculation of reinforced concrete without axial force, the approximate value [$z = 0.9d$] may generally be used [$mm$].
        n_ed: KN
            [$N_{Ed}$] Design value of axial force [$kN$].
        """
        super().__init__()
        self.v_ed = v_ed
        self.a_l = a_l
        self.z = z
        self.n_ed = n_ed

    @staticmethod
    def _evaluate(
        v_ed: KN,
        a_l: MM,
        z: MM,
        n_ed: KN,
    ) -> KN:
        """For more detailed documentation see the class docstring."""
        raise_if_negative(z=z, a_l=a_l)
        return abs(v_ed) * a_l / z + n_ed

    def latex(self, n: int = 2) -> LatexFormula:
        """Returns LatexFormula object for formula 9.3."""
        return LatexFormula(
            return_symbol=r"F_E",
            result=f"{self:.{n}f}",
            equation=r"|V_{Ed}| \cdot a_l / z + N_{Ed}",
            numeric_equation=rf"|{self.v_ed:.{n}f}| \cdot {self.a_l:.{n}f} / {self.z:.{n}f} + {self.n_ed:.{n}f}",
            comparison_operator_label="=",
        )
