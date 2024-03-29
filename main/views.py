from django.shortcuts import render
from django.http import JsonResponse

# rest framework imports
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
  routes =[
    'index'
  ]
  return Response(routes)
