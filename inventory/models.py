from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse

# Create your models here.

class Csv(models.Model):
    file_name = models.FileField(upload_to="excelFiles")
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     return reverse('inventory_home')

    def __str__(self):
        return f"files id:{self.id}"


category_choices =  (
    ('Food', 'food'),
    ('Drinks', "drinks")
)

subcateg_choices = (
    ('Appetizer', 'appetizer'),
    ('Sandwiches', 'sandwiches'),
    ('Burgers', "burgers"),
    ('Salads', "salads"),
    ('Vegeterian', "vegeterian"),
    ('Maindishes', "maindishes"),
    ('Soups', "soups"),
    ('Pizza', "pizza"),
    ('Dessert', 'dessert'),
    ('Cocktail', "cocktail"),
    ('Coffee', "coffee")
)

class Products(models.Model):
    items = models.CharField(max_length=100)
    category = models.CharField(choices=category_choices, max_length=100)
    subcategory = models.CharField(choices=subcateg_choices, max_length=100)
    price = models.FloatField(max_length=100)

    # def get_absolute_url(self):
    #     return reverse("inventory_home")

    def __str__(self):
        return f"{self.items}"


