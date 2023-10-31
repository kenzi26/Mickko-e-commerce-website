from django.contrib import admin
from .models import Testimonial

# Register your models here.
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Testimonial._meta.fields]
