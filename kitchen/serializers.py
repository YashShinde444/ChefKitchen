from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from kitchen.models import Customer,Location

class LocationSerializer(serializers.Serializer):
    class Meta:
        model = Location
        fields = ['country'] 
        #abstract = True  

class CustomerSerializer(ModelSerializer):
    location = LocationSerializer(many=True)
    class Meta:
        model = Customer
        fields = ['name','email','mobileno','location']