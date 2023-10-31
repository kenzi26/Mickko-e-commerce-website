from django.contrib import admin
from .models import ContactUs

# Register your models here.
@admin.register(ContactUs)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ContactUs._meta.fields]
