# coding: utf-8
import math

class CalcPrice:
    """
    税抜価格から税込価格を算出する。（またはその逆）
    """

    # 税率
    TAX_RATE_NORMAL = 10
    TAX_RATE_REDUCED = 8
    # 端数取り扱い
    ROUNDING_MODE_FLOOR = "1"
    ROUNDING_MODE_ROUND = "2"
    ROUNDING_MODE_CEIL  = "3"

    def __init__(self, rounding_mode:str="1"):
        """
        初期化

        Args:
            rounding_mode str:
                端数取り扱い（1:切り捨て、2:四捨五入、3:切り上げ）
        """
        self.rounding_mode = rounding_mode


    def include_tax_price(self, item_price:int, tax_rate:int) -> int:
        """
        税込価格計算

        Args:
            item_price int:
                本体価格
            tax_rate int:
                税率
        Returns:
            int:
                税込価格
        """
        tax_price = item_price * (tax_rate / 100)
        include_tax_price = item_price + tax_price
        if (self.rounding_mode == CalcPrice.ROUNDING_MODE_FLOOR):
            return math.floor(include_tax_price)
        elif (self.rounding_mode == CalcPrice.ROUNDING_MODE_ROUND):
            return math.round(include_tax_price)
        else:
            return math.ceil(include_tax_price)

    def exclude_tax_price(self, item_price:int, tax_rate:int) -> int:
        exclude_tax_price = item_price / (tax_rate / 100 + 1)
        if (self.rounding_mode == CalcPrice.ROUNDING_MODE_FLOOR):
            return math.floor(exclude_tax_price)
        elif (self.rounding_mode == CalcPrice.ROUNDING_MODE_ROUND):
            return math.round(exclude_tax_price)
        else:
            return math.ceil(exclude_tax_price)

    def get_tax_rate(self):
        pass
