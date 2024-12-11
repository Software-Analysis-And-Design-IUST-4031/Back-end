import csv
from utils.models import City

def populate_cities_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city_name = row['city'].strip()  
            country_iso3 = row['iso3'].strip() 
            City.objects.get_or_create(name=city_name, iso3=country_iso3)
        print("Database successfully populated!")


