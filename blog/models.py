from django.db import models
from accounts.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Blog(models.Model):
    title=  models.CharField(max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='blog-image/', null=True, blank=True) 
    content=models.CharField(max_length=500)
    date_published= models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_deleted = models.BooleanField()


    @property
    def author_name(self):
        return  self.author.full_name
    
    #for soft delete
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
        
    #for restoring after soft delete
    def restore(self):
        self.is_deleted = False
        self.save()
        
    def __str__(self):
        return self.title
