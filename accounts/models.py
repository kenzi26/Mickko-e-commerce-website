from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    """Create super user"""

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):    #full name instead of first-name and last name, signup is email, username and password
    user_roles= [('user', 'user'), ('admin', 'admin')]
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=12, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=150)
    last_name= models.CharField(max_length=99)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=50, choices= user_roles, default='user')
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'		
    REQUIRED_FIELDS = ['first_name', 'last_name' ]

    objects = UserManager()

    def __str__(self):
        self.phone
        return self.email


