from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
  def create(self,validated_data):
    return User.objects.create_user(**validated_data)
  
  class Meta:
    model = User
    fields = ['id','name', 'email', 'password','phone','created_at']
    extra_kwargs = {
      'password' : {'write_only': True}
    }

class ProductMediaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product_media
    fields = '__all__'

  def get_image(self,product_media):
    request = self.content.get('request')
    return request.bulld_absolute_uri(product_media.image.url)
  
class ProductSpecificationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product_specification
    fields = '__all__'  


class ProductSerializer(serializers.ModelSerializer):
  category = serializers.SerializerMethodField()
  class Meta:
    model = Product
    fields = '__all__'

  def get_image(self,product):
    request = self.context.get('request')
    return request.build_absolute_uri(product.image.url)
  
  def get_category(self,product):
    return product.category.name
  

class ProductDetailsSerializer(serializers.ModelSerializer):
  category = serializers.SerializerMethodField()
  media = serializers.SerializerMethodField()
  specifications = serializers.SerializerMethodField()
  class Meta:
    model = Product
    fields = '__all__'

  def get_image(self,product):
    request = self.context.get('request')
    return request.build_absolute_uri(product.image.url)
  
  def get_category(self,product):
    return product.category.name
  
  def get_media(self,product):
    product_images = Product_media.objects.filter(product=product)
    serializer = ProductMediaSerializer(product_images, many=True, context={
      'request': self.context.get('request')
    })
    return serializer.data
  
  def get_specifications(self,product):
    product_specifications = Product_specification.objects.filter(product=product).first()
    serializer = ProductSpecificationSerializer(product_specifications)
    return serializer.data
