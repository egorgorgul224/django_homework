from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.management import call_command


class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', ('categories_fixture.json', 'products_fixture.json',))
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixtures'))
