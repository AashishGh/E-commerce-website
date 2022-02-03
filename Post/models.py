from django.db import models
from phone_field import PhoneField
from django.core.validators import RegexValidator
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    Title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{10}$', message="Phone number must be 10 digits and  entered in the format: '98XXXXXXXX'.")
    contact_number = models.CharField(
        validators=[phone_regex], max_length=13)  # validators should be a list
    image1 = models.ImageField(upload_to='images/', default=True)
    selling_price = models.PositiveIntegerField()
    GoogleMap_Location = models.URLField(max_length=200, null=True)
    description = models.TextField()
    return_policy = models.CharField(max_length=300, null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0) 
    
    
    def __str__(self):
        return self.Title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images/")

    def __str__(self):
        return self.product.title