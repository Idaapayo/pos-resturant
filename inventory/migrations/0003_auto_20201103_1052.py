# Generated by Django 2.2.7 on 2020-11-03 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20201029_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='subcategory',
            field=models.CharField(choices=[('Appetizer', 'appetizer'), ('Sandwiches', 'sandwiches'), ('Burgers', 'burgers'), ('Salads', 'salads'), ('Vegeterian', 'vegeterian'), ('Maindishes', 'maindishes'), ('Soups', 'soups'), ('Pizza', 'pizza'), ('Dessert', 'dessert'), ('Cocktail', 'cocktail'), ('Coffee', 'coffee')], max_length=100),
        ),
    ]
