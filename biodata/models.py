from django.db import models
from solo.models import SingletonModel
from django.contrib.postgres.fields import ArrayField

class BioData(SingletonModel):
    """ Hero model that enables the home page and it's content to be dynamic. It only takes one instance"""
    work_emails = emails = ArrayField(models.EmailField(), help_text="Enter email addresses separated by commas.") 
    phone_numbers = (models.CharField(max_length=15))
    sales_email = models.EmailField()
    contact_us_email = models.EmailField()
    footer_text = models.TextField()

    #when you change the DB, make emails and phone_numbers to be array
    
    class Meta:
        verbose_name_plural = 'Bio Data'

