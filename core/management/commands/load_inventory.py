from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from core.models import Product
from django.core.files import File

def get_path(file):
    return os.path.join(settings.BASE_DIR, 'inventory', file)

class Command(BaseCommand):
    help = "Load inventory onto site"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        print('Deleting inventory')
        Product.objects.all().delete()
        with open(get_path('inventory.csv'), 'r') as file:
            reader = csv.DictReader(file)
            i = 0
            for row in reader:
                i += 1
                product = Product(
                    title=row['title'],
                    price=row['price'],
                    details=row['details'],
                  
                )
                product.image.save(row['image'],
                                    File(open(get_path(row['image']), 'rb')))
                
                # product.save()
        print(f"{i} products loaded!")                    
