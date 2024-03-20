from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from rest_framework.decorators import api_view

from .models import menu
from .serializers import MenuSerializer

def sayHello(request):
    return HttpResponse("Hello World")

# Create your views here.

def index(request):
    return render(request,'index.html',{})

class MenuItemView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

