from django.shortcuts import render

from rest_framework import generics
from .models import PizzaOrder
from .serializers import PizzaOrderSerializer

# Create your views here.
class PizzaOrderList(generics.ListCreateAPIView):
    queryset = PizzaOrder.objects.all()
    serializer_class = PizzaOrderSerializer