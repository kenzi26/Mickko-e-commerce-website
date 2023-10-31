from django.db import models
from django.utils.text import slugify

class ProductCategory(models.Model):

    slug = models.SlugField(max_length=100, null=False, blank=True)
    icon = models.ImageField(upload_to="product_categories", null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400, blank=True)
    display_order = models.SmallIntegerField(null=False, blank=True, default=0)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField( null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    #for soft delete
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
        

    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["display_order"]
        verbose_name_plural = 'Product Categories'