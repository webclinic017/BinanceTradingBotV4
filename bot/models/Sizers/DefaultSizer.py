from models.Sizers.Sizer import Sizer as Sizer
import backtrader as bt
from dataclasses import dataclass
from dataclasses import field


@dataclass
class DefaultSizer(Sizer):
    sizer: bt.Sizer = bt.sizers.PercentSizer
    parameters: dict = field(default_factory=lambda: {"percents":99})

