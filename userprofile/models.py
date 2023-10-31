from django.db import models
from user.models import User 

class UserProfile(models.Model):
    """ This uses the django user model to return profile details about a user."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=255, null=True)

    @property
    def email(self):
        return self.user.email
    @email.setter
    def email(self, value):
        self.user.email = value
        self.user.save()
    @property
    def full_name(self):
        return self.user.full_name
    @full_name.setter
    def full_name(self, value):
        self.user.full_name = value
        self.user.save()
    def __str__(self):
        return self.user.username
