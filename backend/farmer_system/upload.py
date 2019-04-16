
from jica.models import District, Subcounty, Parish

import csv

# importing models where i want to upload content

def upload_content():
        file_open =open('./locations.csv')
    # reads the file
        read = csv.reader(file_open)
        
        for d,s,p in read:
# gets the district or subcounty if it already exists and attcahes the foreign keys to it in case its in the db else creates if its new
                district,created = District.objects.get_or_create(name=d)
                subcounty,created = Subcounty.objects.get_or_create(name=s, district=district)
                # creates parishes for asubcounty also displays the one to many relation ship
                Parish.objects.create(name=p, subcounty=subcounty)
                
                print(f'added {d} , {s}, {p}')
        return'Created'


upload_content()       
        
 