from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

class ManagerCustomeUser(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('email is required')
        ne=self.normalize_email(email).islower()
        CUO=self.model(email=ne,first_name=first_name,last_name=last_name)
        CUO.set_password(password)
        CUO.save()
        return CUO
    def create_superuser(self,email,first_name,last_name,password):
        CUO=self.create_user(email,first_name,last_name,password)
        CUO.is_staff=True
        CUO.is_superuser=True
        CUO.save()
class CustomUser(AbstractBaseUser,PermissionsMixin): 
    email=models.EmailField(primary_key=True)
    first_name=models.CharField()
    last_name=models.CharField()
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects=ManagerCustomeUser()
    USERNAME_FIELD='email'               
    REQUIRED_FIELDS=['first_name','last_name']