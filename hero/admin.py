from django.contrib import admin
from .models import Hero

# Register your models here.
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('Header', 'text', 'image')
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        existing_instance = Hero.objects.exists()
        if existing_instance:
            return False
        else:
            return True
