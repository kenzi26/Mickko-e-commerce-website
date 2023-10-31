from django.contrib import admin
from quotation.models import Quotation
from quotation_item.models import QuotationItem
# Register your models here.

@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'display_quotation_items', 'message', 'user', 'status', 'date', 'product_images', 'product_name')
    def display_quotation_items(self, obj):
        return ", ".join([str(p) for p in obj.quotation_items.all()])

    display_quotation_items.short_description = 'Quotationitems'
