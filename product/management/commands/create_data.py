from django.core.management.base import BaseCommand
from product.models import Category, Product
import requests
from django.utils.text import slugify

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Creating data...")
        response = requests.get('https://fakestoreapi.com/products')
        products = response.json()
        
        # Track categories we've already created
        categories = {}
        
        for product_data in products:
            category_name = product_data['category']
            
            # Create category if it doesn't exist
            if category_name not in categories:
                categories[category_name] = Category.objects.create(
                    name=category_name,
                    description=f"Products in {category_name} category"
                )
            
            # Create product using existing category
            Product.objects.create(
                name=product_data['title'],
                description=product_data['description'],
                price=product_data['price'],
                stock=100,  # Default stock value
                image=product_data['image'],
                category=categories[category_name],
                is_active=True
            )
            
        print("Data created successfully")