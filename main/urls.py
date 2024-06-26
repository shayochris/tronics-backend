from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)

urlpatterns =[
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

  path('',views.index, name='index'),
  path('signup/', views.signup, name='signup'),
  path('login/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('products/', views.products),
  path('product/<str:id>/', views.product)
]