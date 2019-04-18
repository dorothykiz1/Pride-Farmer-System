from rest_framework import serializers

from .models import District,Subcounty,Parish,Farmer,Harvest,Officer,Season
 
class DistrictSerializer(Serializers.ModelSerializer):
     
    class Meta:
        model= District
        fields = "__all__"

class SubcountySerializer(Serializers.ModelSerializer):
     
    class Meta:
        model= Subcounty
        fields = "__all__"

class ParishSerializer(Serializers.ModelSerializer):
     
    class Meta:
        model= Parish
        fields = "__all__"

class FarmerSerializer(Serializers.ModelSerializer):
     
    class Meta:
        model= Farmer
        fields = "__all__"

class HarvestSerializer(Serializers.ModelSerializer):
     
    class Meta:
        model= Harvest
        fields = "__all__"

class OfficerSerializer(Serializers.ModelSerializer):
     
    class Meta:
        model= Officer
        fields = "__all__"

class SeasonSerializer(Serializers.ModelSerializer):
     
    class Meta:
        model= Season
        fields = "__all__"

