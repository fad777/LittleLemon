from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics,viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import menu, booking
from .serializers import MenuSerializer, BookingSerializer


@api_view()
@ permission_classes([IsAuthenticated])
def msg(request):
    return HttpResponse({"messagess" : "This view is protected"})


def sayHello(request):
    return HttpResponse("Hello World")

# Create your views here.

def index(request):
    return render(request,'index.html',{})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):

    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = booking.objects.all()
    serializer_class = BookingSerializer
    

