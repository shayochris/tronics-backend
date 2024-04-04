from django.contrib import admin
from .models import *

admin.site.register(
  [
   User, 
   Product_category,
   Product,
   Product_media,
   Product_specification
  ]
)
