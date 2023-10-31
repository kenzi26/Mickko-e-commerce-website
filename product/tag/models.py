from django.db import models
from django.utils.text import slugify

class ProductTag(models.Model):
    slug = models.SlugField(max_length=100, null=False, blank=True)
    icon = models.ImageField(upload_to="product_tags", null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400, blank=True)
    display_order = models.SmallIntegerField(null=False, blank=True, default=0)
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    #for soft delete
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
    

    class Meta:
        ordering = ["display_order"]
        verbose_name_plural = 'Product Tags'

        