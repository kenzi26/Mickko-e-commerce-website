from django.contrib import admin
from .models import Product, ProductBrand, ProductCoupon, ProductTag, ProductCategory, SubCategory
from django.shortcuts import redirect

from product.category.forms import CategoryForm, SubCategoryForm


from django import forms

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ('id', 'name', 'slug', 'description', 'display_sub_categories') 
    
    def display_sub_categories(self, obj):
        return ", ".join([str(p) for p in obj.sub_categories.all()])
    display_sub_categories.short_description = 'SubCategories'
    
    def changelist_view(self, request, extra_context=None):
        if len(request.GET) == 0:
            get_param = "is_prime=True"
            return redirect("{url}?{get_parms}".format(url=request.path, get_parms=get_param))
        return super(CategoryAdmin, self).changelist_view(request, extra_context=extra_context)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    form = SubCategoryForm
    list_display = ('id', 'name', 'slug', 'description') 
    def changelist_view(self, request, extra_context=None):
        if len(request.GET) == 0:
            get_param = "is_prime=False"
            return redirect("{url}?{get_parms}".format(url=request.path, get_parms=get_param))
        return super(SubCategoryAdmin, self).changelist_view(request, extra_context=extra_context)

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