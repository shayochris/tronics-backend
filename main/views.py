from django.shortcuts import render
from django.http import JsonResponse
from .serializers import *

# rest framework imports
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
  routes =[
    'index'
  ]
  return Response(routes)


@api_view(['GET','POST'])
def signup(request):
  if request.method == 'GET':
    data = User.objects.exclude(is_superuser=True)
    serializer = UserSerializer(data, many=True)
    return Response(serializer.data)

  if request.method == 'POST':
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'success':'user created successfully'},status=201)
    else:
      return Response(serializer.errors, status=400)
  