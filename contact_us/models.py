from django.db import models

# Create your models here.
class ContactUs(models.Model):
    full_name= models.CharField(max_length= 255)
    email= models.EmailField()
    phone_number= models.CharField(max_length=15)
    subject= models.CharField(max_length=250)
    message= models.TextField()
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.full_name
    
    #for soft delete
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
        
    #for restoring after soft delete
    def restore(self):
        self.is_deleted = False
        self.save()
    class Meta:
        verbose_name_plural = 'Contact Us'
