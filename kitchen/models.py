#from django.db import models
from djongo import models
# Create your models here.
class Location(models.Model):
    country = models.TextField(null=True,blank=True)
    state = models.TextField(null=True,blank=True)
    city = models.TextField(null=True,blank=True)
    address_line1 = models.TextField(null=True,blank=True)
    address_line2 = models.TextField(null=True,blank=True)
    pincode = models.TextField(null=True,blank=True)
    class Meta:
        abstract = True

    def __str__(self):
        return self.city

class Customer(models.Model):
    name = models.TextField(null=True,blank=True)
    email = models.TextField(null=True,blank=True)
    mobileno = models.TextField(null=True,blank=True)
    location = models.EmbeddedField(model_container=Location)
    def __str__(self):
        return self.name
