from django.contrib import admin
from .models import BioData

# Register your models here.

@admin.register(BioData)
class BioDataFormAdmin(admin.ModelAdmin):
    list_display = ('emails','phone_numbers', 'sales_email')
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        existing_instance = BioData.objects.exists()
        if existing_instance:
            return False
        else:
            return True