from django.core.management.base import BaseCommand
import json
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories(filepath='courses.json'):
        with open(filepath, 'r', encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def json_read_products(filepath='courses.json'):
        with open(filepath, 'r', encoding="utf-8") as f:
            return json.load(f)

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_for_create = []
        for category_data in self.json_read_categories():
            category_for_create.append(
                Category(
                    name=category_data['fields']['name'],
                    description=category_data['fields'].get('description', '')
                )
            )
        Category.objects.bulk_create(category_for_create)

        product_for_create = []
        for product_data in self.json_read_products():
            category = Category.objects.get(name=product_data['fields']['name'])
            product_for_create.append(
                Product(
                    name=product_data['fields']['name'],
                    description=product_data.get('description', ''),
                    price=product_data.get('price', 0),
                    created_at=product_data.get('created_at'),
                    category=category
                )
            )
        Product.objects.bulk_create(product_for_create)

        self.stdout.write(self.style.SUCCESS("Данные успешно загружены в базу данных."))
