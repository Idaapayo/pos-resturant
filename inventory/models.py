from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Csv(models.Model):
    file_name = models.FileField(upload_to="excelFiles")
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"files id:{self.id}"


category_choices =  (
    ('Food', 'food'),
    ('Drinks', "drinks")
)

# subcateg_choices = (
#
# )

class Products(models.Model):
    items = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=category_choices)
    subcategory = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)

    def __str___(self):
        return f"{self.items}"


