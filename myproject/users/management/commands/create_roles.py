
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from products.models import Product 

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        
        admin_group, _ = Group.objects.get_or_create(name='Admin')
        seller_group, _ = Group.objects.get_or_create(name='Seller')
        customer_group, _ = Group.objects.get_or_create(name='Customer')

        
        admin_permissions = Permission.objects.all()  
        admin_group.permissions.set(admin_permissions)

        product_ct = ContentType.objects.get_for_model(Product)
        seller_permissions = Permission.objects.filter(content_type=product_ct) 
        seller_group.permissions.set(seller_permissions)

        customer_permissions = []  
        customer_group.permissions.set(customer_permissions)

        self.stdout.write("Roles and permissions created successfully.")
