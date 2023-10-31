from django.db import models
from user.models import User
import decimal
from product.models import Product


class SpecialOffer(models.Model):
    percentage_off = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price =  models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    _new_price = models.DecimalField(db_column="new_price",max_digits=10, decimal_places=2, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='special_offers/')
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    @property
    def new_price(self):
        discount = decimal.Decimal(self.percentage_off) / decimal.Decimal(100.0)
        new_price = decimal.Decimal(self.price) * decimal.Decimal(1 - discount)
        return round(new_price, 2)
    @new_price.setter
    def my_date(self, value):
        self._new_price = value
    def __str__(self):
        return self.product.name
    
