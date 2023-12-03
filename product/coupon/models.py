from django.db import models

class ProductCoupon(models.Model):

    class Type (models.TextChoices): 
       percentage = ('percentage', 'Percentage')
       fixed = ('fixed', 'Fixed')

    id = models.PositiveIntegerField(primary_key=True)
    code = models.CharField(max_length=150, unique=True)
    value = models.PositiveIntegerField( default=0)
    description = models.TextField(max_length=400, blank=True)
    type = models.CharField(max_length=100, choices=Type.choices, default=Type.fixed, null=False, blank=True)
    expire_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)

    class Meta:
        verbose_name_plural = 'Product Coupons'

