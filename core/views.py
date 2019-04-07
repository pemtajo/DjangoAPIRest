from django.shortcuts import render

from rest_framework import generics
from .models import PizzaOrder, Size, Flavor, Adicional
from .serializers import PizzaOrderSerializer, SizeSerializer, FlavorSerializer, AdicionalSerializer

# Create your views here.
class PizzaOrderList(generics.ListCreateAPIView):
    queryset = PizzaOrder.objects.all()
    serializer_class = PizzaOrderSerializer

class SizeList(generics.ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class FlavorList(generics.ListCreateAPIView):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer

class AdicionalList(generics.ListCreateAPIView):
    queryset = Adicional.objects.all()
    serializer_class = AdicionalSerializer