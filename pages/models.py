from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields.related import ManyToManyField
from django_google_maps import fields as map_fields
from django.urls import reverse
# from accounts.models import User

class Location(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)       

class Picture(models.Model):
    title = models.CharField(max_length=25)

class WorkSite(Location):
    pass



#     def __str__(self):
#         return self.name
    
#     def __repr__(self):
#         return "%s, %s" % (self.name, self.location)



2