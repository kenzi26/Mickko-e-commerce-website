from django.db import models
from django.urls import reverse
from user.models import User 
from quotation_item.models import QuotationItem

  

class Quotation(models.Model):
    """  Quotation model enables users to make orders on products. It also enables frontend team to get 
    a list of quotes made by a user"""


    STATUS_CHOICES = (
        ('pending', 'Pending Payment'),
        ('paid', 'Paid'),
        ('confirmed', 'Confirmed'),
    )

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    quotation_items = models.ManyToManyField(QuotationItem, blank=True)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def product_images(self):
        return [item.product.main_image.url for item in self.quotation_items.all()]

    
    @property
    def product_name(self):
        return [item.product.name for item in self.quotation_items.all()]
