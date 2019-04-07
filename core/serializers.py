from rest_framework import serializers
from .models import PizzaOrder, Size, Flavor, Adicional

class PizzaOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaOrder
        fields = ('size', 'flavor', 'adicionals')
    
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = '__all__'

class AdicionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adicional
        fields = '__all__'

