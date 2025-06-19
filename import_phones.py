import csv
from django.core.management.base import BaseCommand
from your_app.models import Phone
from django.utils.dateparse import parse_date

class Command(BaseCommand):
    help = 'Импорт данных телефонов из CSV файла'

    def handle(self, *args, **options):
        csv_file_path = 'phone_app/data/phones.csv'

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                phone_id = int(row['id'])
                name = row['name']
                image = row['image']
                price = float(row['price'])
                release_date = parse_date(row['release_date'])
                lte_exists = row['lte_exists'].strip().lower() == 'true'

                Phone.objects.update_or_create(
                    id=phone_id,
                    defaults={
                        'name': name,
                        'image': image,
                        'price': price,
                        'release_date': release_date,
                        'lte_exists': lte_exists,
                    }
                )

        self.stdout.write(self.style.SUCCESS('Данные успешно импортированы'))
