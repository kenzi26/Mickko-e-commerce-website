from django.db import models
from django.utils.text import slugify

class ProductBrand(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    slug = models.SlugField(max_length=100, null=False, blank=True)
    icon = models.ImageField(upload_to="product_brands", null=True, blank=True)
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=500, blank=True)
    display_order = models.SmallIntegerField(null=False, blank=True, default=0)
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)
    
    class Meta:
        ordering = ["display_order"]
        verbose_name_plural = 'Product Brands'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name    