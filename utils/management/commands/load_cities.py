import csv
from django.core.management.base import BaseCommand
from django.db.models import Count
from utils.models import City


class Command(BaseCommand):
    help = 'Load cities from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def remove_database_duplicates(self):
        duplicates = (
            City.objects.values('name', 'country')
            .annotate(count=Count('id'))
            .filter(count__gt=1)
        )
        for dup in duplicates:
            # Keep one record and delete the others
            City.objects.filter(name=dup['name'], country=dup['country']).exclude(
                id=City.objects.filter(name=dup['name'], country=dup['country']).first().id
            ).delete()

    def handle(self, *args, **kwargs):
        file_path = kwargs['csv_file']

        try:
            # Clean up existing duplicates
            self.remove_database_duplicates()

            with open(file_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                missing_columns = [col for col in ['city', 'country'] if col not in reader.fieldnames]
                if missing_columns:
                    self.stdout.write(self.style.ERROR(f'Missing columns: {", ".join(missing_columns)}'))
                    return

                processed = set()

                for row in reader:
                    city_name = row['city'].strip()
                    country_name = row['country'].strip()

                    # Skip duplicates within the CSV
                    if (city_name, country_name) in processed:
                        continue

                    processed.add((city_name, country_name))

                    # Use get_or_create to handle duplicates in the database
                    City.objects.get_or_create(name=city_name, country=country_name)

            self.stdout.write(self.style.SUCCESS(f'Successfully loaded cities from {file_path}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
