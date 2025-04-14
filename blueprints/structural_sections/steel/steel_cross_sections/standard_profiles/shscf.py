"""SHSCF Steel Profiles."""

from enum import Enum

from blueprints.type_alias import MM


class SHSCF(Enum):
    """Geometrical representation of SHSCF steel profiles."""

    SHSCF_20_2 = ("SHSCF20x2", 20, 2, 4, 2)
    SHSCF_25_2 = ("SHSCF25x2", 25, 2, 4, 2)
    SHSCF_25_2_5 = ("SHSCF25x2.5", 25, 2.5, 5, 2.5)
    SHSCF_25_3 = ("SHSCF25x3", 25, 3, 6, 3)
    SHSCF_30_2 = ("SHSCF30x2", 30, 2, 4, 2)
    SHSCF_30_2_5 = ("SHSCF30x2.5", 30, 2.5, 5, 2.5)
    SHSCF_30_3 = ("SHSCF30x3", 30, 3, 6, 3)
    SHSCF_40_2 = ("SHSCF40x2", 40, 2, 4, 2)
    SHSCF_40_2_5 = ("SHSCF40x2.5", 40, 2.5, 5, 2.5)
    SHSCF_40_3 = ("SHSCF40x3", 40, 3, 6, 3)
    SHSCF_40_4 = ("SHSCF40x4", 40, 4, 8, 4)
    SHSCF_50_2 = ("SHSCF50x2", 50, 2, 4, 2)
    SHSCF_50_2_5 = ("SHSCF50x2.5", 50, 2.5, 5, 2.5)
    SHSCF_50_3 = ("SHSCF50x3", 50, 3, 6, 3)
    SHSCF_50_4 = ("SHSCF50x4", 50, 4, 8, 4)
    SHSCF_50_5 = ("SHSCF50x5", 50, 5, 10, 5)
    SHSCF_60_2 = ("SHSCF60x2", 60, 2, 4, 2)
    SHSCF_60_2_5 = ("SHSCF60x2.5", 60, 2.5, 5, 2.5)
    SHSCF_60_3 = ("SHSCF60x3", 60, 3, 6, 3)
    SHSCF_60_4 = ("SHSCF60x4", 60, 4, 8, 4)
    SHSCF_60_5 = ("SHSCF60x5", 60, 5, 10, 5)
    SHSCF_60_6 = ("SHSCF60x6", 60, 6, 12, 6)
    SHSCF_60_6_3 = ("SHSCF60x6.3", 60, 6.3, 15.8, 9.4)
    SHSCF_70_2_5 = ("SHSCF70x2.5", 70, 2.5, 5, 2.5)
    SHSCF_70_3 = ("SHSCF70x3", 70, 3, 6, 3)
    SHSCF_70_4 = ("SHSCF70x4", 70, 4, 8, 4)
    SHSCF_70_5 = ("SHSCF70x5", 70, 5, 10, 5)
    SHSCF_70_6 = ("SHSCF70x6", 70, 6, 12, 6)
    SHSCF_70_6_3 = ("SHSCF70x6.3", 70, 6.3, 15.8, 9.4)
    SHSCF_80_3 = ("SHSCF80x3", 80, 3, 6, 3)
    SHSCF_80_4 = ("SHSCF80x4", 80, 4, 8, 4)
    SHSCF_80_5 = ("SHSCF80x5", 80, 5, 10, 5)
    SHSCF_80_6 = ("SHSCF80x6", 80, 6, 12, 6)
    SHSCF_80_6_3 = ("SHSCF80x6.3", 80, 6.3, 15.8, 9.4)
    SHSCF_80_8 = ("SHSCF80x8", 80, 8, 20, 12)
    SHSCF_90_3 = ("SHSCF90x3", 90, 3, 6, 3)
    SHSCF_90_4 = ("SHSCF90x4", 90, 4, 8, 4)
    SHSCF_90_5 = ("SHSCF90x5", 90, 5, 10, 5)
    SHSCF_90_6 = ("SHSCF90x6", 90, 6, 12, 6)
    SHSCF_90_6_3 = ("SHSCF90x6.3", 90, 6.3, 15.8, 9.4)
    SHSCF_90_8 = ("SHSCF90x8", 90, 8, 20, 12)
    SHSCF_100_3 = ("SHSCF100x3", 100, 3, 6, 3)
    SHSCF_100_4 = ("SHSCF100x4", 100, 4, 8, 4)
    SHSCF_100_5 = ("SHSCF100x5", 100, 5, 10, 5)
    SHSCF_100_6 = ("SHSCF100x6", 100, 6, 12, 6)
    SHSCF_100_6_3 = ("SHSCF100x6.3", 100, 6.3, 15.8, 9.4)
    SHSCF_100_8 = ("SHSCF100x8", 100, 8, 20, 12)
    SHSCF_100_10 = ("SHSCF100x10", 100, 10, 25, 15)
    SHSCF_100_12 = ("SHSCF100x12", 100, 12, 36, 24)
    SHSCF_100_12_5 = ("SHSCF100x12.5", 100, 12.5, 37.5, 25)
    SHSCF_120_3 = ("SHSCF120x3", 120, 3, 6, 3)
    SHSCF_120_4 = ("SHSCF120x4", 120, 4, 8, 4)
    SHSCF_120_5 = ("SHSCF120x5", 120, 5, 10, 5)
    SHSCF_120_6 = ("SHSCF120x6", 120, 6, 12, 6)
    SHSCF_120_6_3 = ("SHSCF120x6.3", 120, 6.3, 15.8, 9.4)
    SHSCF_120_8 = ("SHSCF120x8", 120, 8, 20, 12)
    SHSCF_120_10 = ("SHSCF120x10", 120, 10, 25, 15)
    SHSCF_120_12 = ("SHSCF120x12", 120, 12, 36, 24)
    SHSCF_120_12_5 = ("SHSCF120x12.5", 120, 12.5, 37.5, 25)
    SHSCF_140_4 = ("SHSCF140x4", 140, 4, 8, 4)
    SHSCF_140_5 = ("SHSCF140x5", 140, 5, 10, 5)
    SHSCF_140_6 = ("SHSCF140x6", 140, 6, 12, 6)
    SHSCF_140_6_3 = ("SHSCF140x6.3", 140, 6.3, 15.8, 9.4)
    SHSCF_140_8 = ("SHSCF140x8", 140, 8, 20, 12)
    SHSCF_140_10 = ("SHSCF140x10", 140, 10, 25, 15)
    SHSCF_140_12 = ("SHSCF140x12", 140, 12, 36, 24)
    SHSCF_140_12_5 = ("SHSCF140x12.5", 140, 12.5, 37.5, 25)
    SHSCF_150_4 = ("SHSCF150x4", 150, 4, 8, 4)
    SHSCF_150_5 = ("SHSCF150x5", 150, 5, 10, 5)
    SHSCF_150_6 = ("SHSCF150x6", 150, 6, 12, 6)
    SHSCF_150_6_3 = ("SHSCF150x6.3", 150, 6.3, 15.8, 9.4)
    SHSCF_150_8 = ("SHSCF150x8", 150, 8, 20, 12)
    SHSCF_150_10 = ("SHSCF150x10", 150, 10, 25, 15)
    SHSCF_150_12 = ("SHSCF150x12", 150, 12, 36, 24)
    SHSCF_150_12_5 = ("SHSCF150x12.5", 150, 12.5, 37.5, 25)
    SHSCF_150_16 = ("SHSCF150x16", 150, 16, 48, 32)
    SHSCF_160_4 = ("SHSCF160x4", 160, 4, 8, 4)
    SHSCF_160_5 = ("SHSCF160x5", 160, 5, 10, 5)
    SHSCF_160_6 = ("SHSCF160x6", 160, 6, 12, 6)
    SHSCF_160_6_3 = ("SHSCF160x6.3", 160, 6.3, 15.8, 9.4)
    SHSCF_160_8 = ("SHSCF160x8", 160, 8, 20, 12)
    SHSCF_160_10 = ("SHSCF160x10", 160, 10, 25, 15)
    SHSCF_160_12 = ("SHSCF160x12", 160, 12, 36, 24)
    SHSCF_160_12_5 = ("SHSCF160x12.5", 160, 12.5, 37.5, 25)
    SHSCF_160_16 = ("SHSCF160x16", 160, 16, 48, 32)
    SHSCF_180_4 = ("SHSCF180x4", 180, 4, 8, 4)
    SHSCF_180_5 = ("SHSCF180x5", 180, 5, 10, 5)
    SHSCF_180_6 = ("SHSCF180x6", 180, 6, 12, 6)
    SHSCF_180_6_3 = ("SHSCF180x6.3", 180, 6.3, 15.8, 9.4)
    SHSCF_180_8 = ("SHSCF180x8", 180, 8, 20, 12)
    SHSCF_180_10 = ("SHSCF180x10", 180, 10, 25, 15)
    SHSCF_180_12 = ("SHSCF180x12", 180, 12, 36, 24)
    SHSCF_180_12_5 = ("SHSCF180x12.5", 180, 12.5, 37.5, 25)
    SHSCF_180_16 = ("SHSCF180x16", 180, 16, 48, 32)
    SHSCF_200_4 = ("SHSCF200x4", 200, 4, 8, 4)
    SHSCF_200_5 = ("SHSCF200x5", 200, 5, 10, 5)
    SHSCF_200_6 = ("SHSCF200x6", 200, 6, 12, 6)
    SHSCF_200_6_3 = ("SHSCF200x6.3", 200, 6.3, 15.8, 9.4)
    SHSCF_200_8 = ("SHSCF200x8", 200, 8, 20, 12)
    SHSCF_200_10 = ("SHSCF200x10", 200, 10, 25, 15)
    SHSCF_200_12 = ("SHSCF200x12", 200, 12, 36, 24)
    SHSCF_200_12_5 = ("SHSCF200x12.5", 200, 12.5, 37.5, 25)
    SHSCF_200_16 = ("SHSCF200x16", 200, 16, 48, 32)
    SHSCF_220_5 = ("SHSCF220x5", 220, 5, 10, 5)
    SHSCF_220_6 = ("SHSCF220x6", 220, 6, 12, 6)
    SHSCF_220_6_3 = ("SHSCF220x6.3", 220, 6.3, 15.8, 9.4)
    SHSCF_220_8 = ("SHSCF220x8", 220, 8, 20, 12)
    SHSCF_220_10 = ("SHSCF220x10", 220, 10, 25, 15)
    SHSCF_220_12 = ("SHSCF220x12", 220, 12, 36, 24)
    SHSCF_220_12_5 = ("SHSCF220x12.5", 220, 12.5, 37.5, 25)
    SHSCF_220_16 = ("SHSCF220x16", 220, 16, 48, 32)
    SHSCF_250_5 = ("SHSCF250x5", 250, 5, 10, 5)
    SHSCF_250_6 = ("SHSCF250x6", 250, 6, 12, 6)
    SHSCF_250_6_3 = ("SHSCF250x6.3", 250, 6.3, 15.8, 9.4)
    SHSCF_250_8 = ("SHSCF250x8", 250, 8, 20, 12)
    SHSCF_250_10 = ("SHSCF250x10", 250, 10, 25, 15)
    SHSCF_250_12 = ("SHSCF250x12", 250, 12, 36, 24)
    SHSCF_250_12_5 = ("SHSCF250x12.5", 250, 12.5, 37.5, 25)
    SHSCF_250_16 = ("SHSCF250x16", 250, 16, 48, 32)
    SHSCF_260_6 = ("SHSCF260x6", 260, 6, 12, 6)
    SHSCF_260_6_3 = ("SHSCF260x6.3", 260, 6.3, 15.8, 9.4)
    SHSCF_260_8 = ("SHSCF260x8", 260, 8, 20, 12)
    SHSCF_260_10 = ("SHSCF260x10", 260, 10, 25, 15)
    SHSCF_260_12 = ("SHSCF260x12", 260, 12, 36, 24)
    SHSCF_260_12_5 = ("SHSCF260x12.5", 260, 12.5, 37.5, 25)
    SHSCF_260_16 = ("SHSCF260x16", 260, 16, 48, 32)
    SHSCF_300_6 = ("SHSCF300x6", 300, 6, 12, 6)
    SHSCF_300_6_3 = ("SHSCF300x6.3", 300, 6.3, 15.8, 9.4)
    SHSCF_300_8 = ("SHSCF300x8", 300, 8, 20, 12)
    SHSCF_300_10 = ("SHSCF300x10", 300, 10, 25, 15)
    SHSCF_300_12 = ("SHSCF300x12", 300, 12, 36, 24)
    SHSCF_300_12_5 = ("SHSCF300x12.5", 300, 12.5, 37.5, 25)
    SHSCF_300_16 = ("SHSCF300x16", 300, 16, 48, 32)
    SHSCF_350_8 = ("SHSCF350x8", 350, 8, 20, 12)
    SHSCF_350_10 = ("SHSCF350x10", 350, 10, 25, 15)
    SHSCF_350_12 = ("SHSCF350x12", 350, 12, 36, 24)
    SHSCF_350_12_5 = ("SHSCF350x12.5", 350, 12.5, 37.5, 25)
    SHSCF_350_16 = ("SHSCF350x16", 350, 16, 48, 32)
    SHSCF_400_10 = ("SHSCF400x10", 400, 10, 25, 15)
    SHSCF_400_12 = ("SHSCF400x12", 400, 12, 36, 24)
    SHSCF_400_12_5 = ("SHSCF400x12.5", 400, 12.5, 37.5, 25)
    SHSCF_400_16 = ("SHSCF400x16", 400, 16, 48, 32)
    SHSCF_500_12_5 = ("SHSCF500x12.5", 500, 12.5, 37.5, 25)
    SHSCF_500_16 = ("SHSCF500x16", 500, 16, 48, 32)
    SHSCF_500_20 = ("SHSCF500x20", 500, 20, 60, 40)
    SHSCF_600_12_5 = ("SHSCF600x12.5", 600, 12.5, 37.5, 25)
    SHSCF_600_16 = ("SHSCF600x16", 600, 16, 48, 32)
    SHSCF_600_20 = ("SHSCF600x20", 600, 20, 60, 40)

    def __init__(self, alias: str, b: MM, t: MM, r0: MM, ri: MM) -> None:
        """Initialize SHSCF profile.
        Args:
            alias (str): Profile alias.
            b (MM): Total width.
            t (MM): Thickness.
            r0 (MM): Outer radius.
            ri (MM): Inner radius.
        """
        self.alias = alias
        self.total_width = b
        self.total_height = b
        self.thickness = t
        self.inner_radius = ri
        self.outer_radius = r0
        self.center_radius = (r0 + ri) / 2
