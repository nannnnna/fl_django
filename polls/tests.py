from django.test import TestCase
from .models import Category, Product

class CategoryModelTest(TestCase):
    def setUp(self):
        Category.objects.create(title='Тестовая категория')

    def test_category_creation(self):
        category = Category.objects.get(title='Тестовая категория')
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(category.__str__(), category.title)

class ProductModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(title='Тестовая категория')
        Product.objects.create(title='Тестовый продукт', category=category, quantity=50, price=100.0)

    def test_product_creation(self):
        product = Product.objects.get(title='Тестовый продукт')
        self.assertTrue(isinstance(product, Product))
        self.assertEqual(product.__str__(), product.title)
        self.assertEqual(product.quantity, 50)
        self.assertEqual(product.price, 100.0)

    def test_product_category(self):
        product = Product.objects.get(title='Тестовый продукт')
        self.assertEqual(product.category.title, 'Тестовая категория')

class ProductListViewTest(TestCase):
    def setUp(self):
        category = Category.objects.create(title='Тестовая категория')
        Product.objects.create(title='Тестовый продукт', category=category, quantity=50, price=100.0)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/products/')  
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/products/') 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_list.html')  
