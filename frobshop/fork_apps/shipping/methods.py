from oscar.apps.shipping import methods
from oscar.core import prices

from decimal import Decimal as D
from oscar.core import prices


class Yamato(methods.Base):
    code = 'Yamato'
    name = 'ヤマト運輸'

    def calculate(self, basket):
        # 送料は固定で800円の場合
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('80.00'), tax=D('800.00')
        )


class Sagawa(methods.Base):
    code = 'Sagawa'
    name = '佐川急便'

    def calculate(self, basket):
        # 送料は固定で800円の場合
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('100.00'), tax=D('1000.00')
        )