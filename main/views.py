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
  if request.method == 'POST':
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'success':'user created successfully'},status=201)
    else:
      return Response(serializer.errors, status=400)
    

@api_view(['GET'])
def products(request):
  products= Product.objects.all()
  serializer = ProductSerializer(products, many=True, context={'request': request})
  return Response(serializer.data, status=201)


@api_view(['GET','PUT','DELETE'])
def product(request,id):
  product= Product.objects.filter(id=id).first()
  if request.method == 'GET':
    if not product:
      return Response({"error":"No product found"},status=204)
    
    serializer = ProductDetailsSerializer(product, context={'request': request})
    return Response(serializer.data, status=201)
  
  if request.method == 'PUT':
    serializer = ProductSerializer(data=request.data)
    if not serializer.is_valid():
      return Response(serializer.errors,status=400)
    serializer.save()
    return Response({'success': 'product updated'},status=200)
  
  if request.method == 'DELETE':
    product.delete()
    return Response({"success": "product deleted"},status=201)
  