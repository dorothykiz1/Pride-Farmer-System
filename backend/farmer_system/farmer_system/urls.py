"""farmer_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jica import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'districts',views.DistrictAPIView.as_view(),name='Distict_list'),
    path(r'subcounties',views.SubcountyAPIView.as_view(),name='Subcounty_list'),
    path(r'parishes',views.ParishAPIView.as_view(),name='Parish_list'),
    path(r'farmers',views.FarmerAPIView.as_view(),name='Farmer_list'),
    path(r'harvests',views.HarvestAPIView.as_view(),name='Harvest_list'),
    path(r'officers',views.OfficerAPIView.as_view(),name='Officer_list'),
    path(r'seasons',views.SeasonAPIView.as_view(),name='Season_list'),


]
