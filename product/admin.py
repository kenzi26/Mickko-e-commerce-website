from django.contrib import admin
from .models import Product, ProductBrand, ProductCoupon, ProductTag, ProductCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]
@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductBrand._meta.fields]
@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductTag._meta.fields]
    
@admin.register(ProductCoupon)
class ProductCouponAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCoupon._meta.fields]

# @admin.register(ProductCombo)
# class ProductComboAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in ProductCombo._meta.fields]    