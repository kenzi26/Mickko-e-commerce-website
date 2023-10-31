from django.db import models
from product.models import Product

  

class QuotationItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        self.product_name = self.product.name
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Quotation Items'

    def __str__(self):
        return self.product.name
    