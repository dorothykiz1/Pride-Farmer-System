from django.shortcuts import render
from rest_framework import generics
from .models import District,Subcounty,Parish,Farmer,Harvest,Officer,Season
from .serializers import DistrictSerializer,SubcountySerializer,ParishSerializer,FarmerSerializer,HarvestSerializer,OfficerSerializer,SeasonSerializer
 
# Create your views here.
class DistrictAPIView(generics.ListCreateAPIview):
    query = District.objects.all()
    serializer_class =DistrictSerializer

class SubcountyAPIView(generics.ListCreateAPIview):
    query = Subcounty.objects.all()
    serializer_class =SubcountySerializer


class ParishAPIView(generics.ListCreateAPIview):
    query = Parish.objects.all()
    serializer_class = ParishSerializer

class FarmerAPIView(generics.ListCreateAPIview):
    query = Farmer.objects.all()
    serializer_class =FarmerSerializer

class HarvestAPIView(generics.ListCreateAPIview):
    query = Harvest.objects.all()
    serializer_class =HarvestSerializer

class OfficerAPIView(generics.ListCreateAPIview):
    query = Officer.objects.all()
    serializer_class =OfficerSerializer

class SeasonAPIView(generics.ListCreateAPIview):
    query = Season.objects.all()
    serializer_class =SeasonSerializer    