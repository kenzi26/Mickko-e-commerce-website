from django.contrib import admin
from quotation_item.models import QuotationItem
# Register your models here.
@admin.register(QuotationItem)
class QuotationItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'product_name')