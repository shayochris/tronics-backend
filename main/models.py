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
  created_at = models.DateTimeField(auto_now_add = True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)

  objects = CustomUserManager()
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  def __str__(self):
    return f'{self.name}'
  
class Product_category(models.Model):
  name=models.CharField(max_length=255)
  class Meta:
    verbose_name = 'Product_category'
    verbose_name_plural = 'Product_categories'

  def __str__(self):
    return f'{self.name}'

class Product(models.Model):
  name = models.CharField(max_length=255)
  category = models.ForeignKey(Product_category, on_delete=models.CASCADE)
  price = models.FloatField()
  description = models.TextField()
  image = models.ImageField(upload_to = 'products_media')

  def __str__(self):
    return f'{self.name}'
  
class Product_media(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  image = models.ImageField(upload_to = 'products_media')

  def __str__(self):
    return f'{self.product.name}\'s media'
  
class Product_specification(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  memory = models.CharField(max_length=255,null=True,blank=True)
  selfie_camera = models.CharField(max_length=255,null=True,blank=True)
  main_camera = models.CharField(max_length=255,null=True,blank=True)
  display = models.CharField(max_length=255,null=True,blank=True)
  ram = models.CharField(max_length=255,null=True,blank=True)
  os = models.CharField(max_length=255,null=True,blank=True)
  network = models.CharField(max_length=255,null=True,blank=True)
  ram = models.CharField(max_length=255,null=True,blank=True)
  hdd = models.CharField(max_length=255,null=True,blank=True)
  special_feature = models.CharField(max_length=255,null=True,blank=True)
  battery = models.CharField(max_length=255,null=True,blank=True)
  


