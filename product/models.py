from django.db import models

from .brand.models import ProductBrand
from .category.models import ProductCategory 
from .coupon.models import ProductCoupon
from .tag.models import ProductTag
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, editable=False, blank=True)
    featured_image = models.ImageField(upload_to="product_categories", null=True, blank=True)
    description = models.TextField(max_length=400, blank=True)
    details = RichTextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    brand = models.ForeignKey('ProductBrand', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('ProductCategory', on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(ProductTag, blank=True)
    is_favourite= models.BooleanField(default=False)
    related_products = models.ManyToManyField('self',blank= True)
    average_rating = models.DecimalField(max_digits=3, max_length=5,decimal_places=2, null=True, blank= True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
        #for soft delete
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
        
    #for restoring after soft delete
    def restore(self):
        self.is_deleted = False
        self.save()

  

