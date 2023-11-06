from django.db import models

# Create your models here.
class Testimonial(models.Model):
    full_name= models.CharField(max_length=255)
    profile_picture= models.ImageField(upload_to='testimonial/', null=True, blank=True)
    company= models.CharField(max_length=255, null=True, blank=True)
    content= models.CharField(max_length=500)


    class Meta:
       verbose_name_plural = 'Testimonials'
