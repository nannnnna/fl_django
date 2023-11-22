from .models import Category, Product

def load_categories(data):
    for line in data.strip().split("\n")[1:]:
        id, title, _ = line.split(":")
        Category.objects.update_or_create(
            id=int(id),
            defaults={'title': title}
        )

def set_category_parents(data):
    for line in data.strip().split("\n")[1:]:
        id, _, parent = line.split(":")
        category = Category.objects.get(id=int(id))
        if parent != 'None':
            parent_obj = Category.objects.get(id=int(parent))
            category.parent = parent_obj
            category.save()
            
def load_products(data):
    for line in data.strip().split("\n")[1:]: 
        parts = line.split(":", 4)
        if len(parts) != 5:
            print(f"Некорректный формат строки: {line}")
            continue

        id, title, category_id, quantity, price = parts
        try:
            category = Category.objects.get(id=int(category_id))
            Product.objects.update_or_create(
                id=int(id),
                defaults={
                    'title': title, 
                    'category': category, 
                    'quantity': int(quantity), 
                    'price': float(price)
                }
            )
        except Category.DoesNotExist:
            print(f"Категория с ID {category_id} не найдена для продукта {title}.")
        except ValueError as e:
            print(f"Ошибка преобразования данных для продукта {title}: {e}")
            
