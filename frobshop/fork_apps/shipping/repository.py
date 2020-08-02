from oscar.apps.shipping import repository
from oscar.apps.shipping import methods
from . import methods as mymethods
from decimal import Decimal as D


class Repository(repository.Repository):
    methods = (methods.Free(), mymethods.Yamato())

    def get_available_shipping_methods(
            self, basket, shipping_addr=None, **kwargs):
        if basket.total_excl_tax < D('2000.00'):
            self.methods = (mymethods.Yamato(),)
        elif basket.total_excl_tax < D('4000.00'):
            self.methods = (mymethods.Sagawa(), )
        else:
            self.methods = (methods.Free(),)

        return self.methods
