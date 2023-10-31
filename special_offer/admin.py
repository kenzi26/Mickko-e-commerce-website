from django.contrib import admin
from .models import SpecialOffer

@admin.register(SpecialOffer)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SpecialOffer._meta.fields]