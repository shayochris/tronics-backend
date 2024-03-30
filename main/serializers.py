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
