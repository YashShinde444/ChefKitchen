from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer
# Create your views here.

class CrudCustomer(APIView):
    def post(self,request):
        obj = Customer()
        obj.name = request.data['name']
        obj.email = request.data['email']
        obj.mobileno = request.data['mobileno']
        obj.location = {
            'country':request.data['country'],
            'state':request.data['state'],
            'city':request.data['city'],
            'address_line1':request.data['address_line1'],
            'address_line2':request.data['address_line2'],
            'pincode':request.data['pincode'],
        }
        obj.save()
        return Response(status=status.HTTP_200_OK)

    def get(self,request):
        obj = Customer.objects.all()
        serialize = CustomerSerializer(obj,many=True)
        return Response(data=serialize.data,status=status.HTTP_200_OK)


