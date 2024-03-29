from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, UserManager


class CustomUserManager(UserManager):
  def _create_user(self,email,password, **other_fields):
    if not email:
      raise ValueError('email is required')
    
    email = self.normalize_email(email)
    user = self.model(email=email, **other_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_user(self,email,password,**other_fields):
    other_fields.setdefault('is_staff', False)
    other_fields.setdefault('is_superuser', False)
    return self._create_user(email,password,**other_fields)
  
  def create_superuser(self,email,password,**other_fields):
    other_fields.setdefault('is_staff', True)
    other_fields.setdefault('is_superuser', True)
    return self._create_user(email,password,**other_fields)
  

class User(AbstractBaseUser,PermissionsMixin):
  name = models.CharField(max_length = 50)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=255)
  phone = models.CharField(max_length = 20,null=True, blank=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)

  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  def __str__(self):
    return f'{self.name}'