from django.contrib import admin

# Register your models here.
from .models import Category, Product, ProductImage
admin.site.register([Category, Product, ProductImage])