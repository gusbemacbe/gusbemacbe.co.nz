from django.contrib import admin
from .models import Product, ProductAdmin

admin.site.register(Product, ProductAdmin)
