from django.db import models
from decimal import Decimal


class Category(models.Model):
    title = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title
    def get_category_hierarchy(self):
        categories = []
        category = self
        while category:
            categories.append(category.title)
            category = category.parent
        return ' · '.join(reversed(categories))

class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def save(self, *args, **kwargs):
        if self.quantity < 0:
            print(f"Ошибка: значение quantity ({self.quantity}) меньше нуля. Элемент не будет сохранен.")
            return
        if self.quantity > 100000:
            print(f"Ошибка: значение quantity ({self.quantity}) больше максимально допустимого значения. Элемент не будет сохранен.")
            return
        if self.price < 0.0:
            print(f"Ошибка: значение price ({self.price}) меньше нуля. Элемент не будет сохранен.")
            return

        super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
