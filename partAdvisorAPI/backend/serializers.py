from rest_framework import serializers
from .models import Tire, Vehicle

class TireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tire
        fields = ['id', 'model_id', 'brand', 'model', 'tireSpecs', 'mevsim', 'fuelNote', 'performance', 'price']

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['model_id', 'user_id', 'brand', 'model', 'fuelType', 'tireSpecs', 'tireWidth','tireHeight', 'rimSize']
