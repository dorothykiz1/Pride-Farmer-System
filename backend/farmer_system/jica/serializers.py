from rest_framework import serializers

from .models import District,Subcounty,Parish,Farmer,Harvest,Officer,Season
 
class DistrictSerializer(serializers.ModelSerializer):
     
    class Meta:
        model= District
        fields = "__all__"

class SubcountySerializer(serializers.ModelSerializer):
     
    class Meta:
        model= Subcounty
        fields = "__all__"

class ParishSerializer(serializers.ModelSerializer):
     
    class Meta:
        model= Parish
        fields = "__all__"

class FarmerSerializer(serializers.ModelSerializer):
     
    class Meta:
        model= Farmer
        fields = "__all__"

class HarvestSerializer(serializers.ModelSerializer):
     
    class Meta:
        model= Harvest
        fields = "__all__"

class OfficerSerializer(serializers.ModelSerializer):
     
    class Meta:
        model= Officer
        fields = "__all__"

class SeasonSerializer(serializers.ModelSerializer):
     
    class Meta:
        model= Season
        fields = "__all__"

