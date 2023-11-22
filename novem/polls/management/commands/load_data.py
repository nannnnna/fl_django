from django.core.management.base import BaseCommand
from polls.utils import load_categories, load_products

class Command(BaseCommand):
    help = 'Load data into the database'

    def handle(self, *args, **kwargs):
        categories = """
id:title:parent
1:Велосипеды:None
2:Кастрюли:4
3:Тарелки:4
4:Посуда для кухни:5
5:Товары для дома:None
"""
        products = """
id:title:category_id:count:cost
1:Велосипед:1:100:100.50
2:Кастрюля 1,5л:2:50:1200
3:Тарелка 25см:3:1000:25
4:Кастрюля 3л:2:55:300.78
""" 

        load_categories(categories)
        load_products(products)
        self.stdout.write(self.style.SUCCESS('Successfully loaded data'))
