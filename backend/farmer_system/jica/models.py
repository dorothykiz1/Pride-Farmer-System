from django.db import models
from django.contrib.auth.models import User

class District(models.Model):
    """
        The District  model
    """

    # district_code =models.CharField("District Code", max_length=50)
    name =models.CharField( max_length=50)
    # region=models.CharField("Region", max_length=50)
    # sub_region=models.CharField("Sub Region", max_length=50)
    # house_holds=models.IntegerField("Households")
    # population=models.IntegerField("Population")
    # urban_2014=models.IntegerField("Urban code")

    def __str__(self):
        return self.name

class Subcounty(models.Model):
    """
        The Subcounty model
    """
    
    name =models.CharField( max_length=50) 
    district=models.ForeignKey("District", verbose_name="District.name", on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Parish(models.Model):
    """
        The Parish model
    """
    name =models.CharField( max_length=50) 
    subcounty=models.ForeignKey("Subcounty",verbose_name="Subcounty.name", on_delete=models.CASCADE)


    def __str__(self):
        return self.name


farmerchoices =(
    ('ADD FARMER','ADD FARMER'),
    ('FARMER_LIST','FARMER DIRECTORY'),
    ('FARMER_DISTRICTS','FARMER DISTRICTS'),
)
gender_choices=(
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
)
marriage_choices=(
    ('SINGLE','SINGLE'),
    ('MARRIED','MARRIED'),
    ('ENGAGED','ENGAGED'),

)
lang_choices=(
    ('ENGLISH','ENGLISH'),
    ('lUGANDA','LUGANDA'),
    ('RUTOORO','RUTORO'),
)
harvest_choices=(
    ('DRY','DRY'),
    ('WET','WET')
)
class Farmer(models.Model):
    """
      The Farmer model
    """
    name = models.CharField(max_length=50)
    district_id =models.ForeignKey("District", verbose_name="District.id", on_delete=models.CASCADE)
    subcounty_id =models.ForeignKey("Subcounty", verbose_name="Subcounty.id", on_delete=models.CASCADE)
    parish =models.ForeignKey("Parish", verbose_name="Parish.name", on_delete=models.CASCADE)
    village =models.CharField( max_length=50)
    gender =models.CharField(choices = gender_choices ,max_length=50)
    birth_year=models.IntegerField("Birth Year")
    marriage=models.CharField( choices = marriage_choices, max_length=50)
    language=models.CharField(choices=lang_choices ,max_length=50)
    phone=models.CharField(max_length=50)
    photo=models.FileField(upload_to=None, max_length=100)
    community_status=models.BooleanField("Community Status")
    instructor_possibility=models.BooleanField("Instructor Possibility")
    farm_area=models.CharField( max_length=50)
    crop_type=models.CharField( max_length=50)
    past_harvests=models.CharField(choices=harvest_choices, max_length=50)
    latitude=models.DecimalField( max_digits=5, decimal_places=2)
    longitude =models.DecimalField("Longitude", max_digits=5, decimal_places=2)


    def __str__(self):
        return self.name ,self,parish

class Harvest(models.Model):
    """
        The Harvest model
    """
    name =models.CharField( max_length=50)
    season =models.CharField( max_length=50)
    Area =models.CharField( max_length=50)
    harvest=models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Officer(models.Model):
    """
        The Officer model
    """
    name= models.CharField( max_length=50)
    loginID=models.CharField( max_length=50)
    password = models.CharField( max_length=50)
    district=models.ForeignKey("District", verbose_name="", on_delete=models.CASCADE)
    subcountry=models.ForeignKey("Subcounty", verbose_name="", on_delete=models.CASCADE)
    telephone=models.CharField( max_length=50)

    def __str__(self):
        return self.name

class Season(models.Model):
    """ 
        The Season model
    """   
    name = models.CharField( max_length=50)


    def __str__(self):
        return self.name
