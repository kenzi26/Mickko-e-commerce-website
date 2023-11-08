from django.db import models
from solo.models import SingletonModel
from django.contrib.postgres.fields import ArrayField

class Hero(SingletonModel):
    """ Hero model that enables the home page and it's content to be dynamic. It only takes one instance"""

    Header = models.TextField()
    text =  models.TextField() 
    image = models.ImageField(upload_to='hero_images/')
    phone_numbers = models.CharField(max_length=15, blank=True, null=True)
    content= models.CharField(max_length=15, blank=True, null=True)


    def __str__(self):
        return self.Header
