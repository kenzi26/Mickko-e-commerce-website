from django.db import models
from django.utils.text import slugify

class ProductCategory(models.Model):

    priority = models.IntegerField(default=0, help_text="Enter priority list order by lowest to highest. 0 is at the start of the list")
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, null=False, blank=True)
    icon = models.ImageField(upload_to="product_categories", null=True, blank=True)
    description = models.TextField(max_length=400, blank=True)
    sub_category = models.ManyToManyField('self', blank=True)
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
        verbose_name_plural = 'Product Categories'


app_label, *_ = __name__.partition('.')        
class SubCategory(ProductCategory):
    class Meta:
        managed = False
        auto_created = False
        proxy=ProductCategory
        db_table = "%s_%s" % (app_label, "ProductCategory")
        verbose_name_plural = 'SubCategories'
        
    """SubCategory model consists of name and slug input fields"""
    