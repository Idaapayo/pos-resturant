# Generated by Django 2.2.7 on 2020-10-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='subcategory',
            field=models.CharField(choices=[('Food', 'food'), ('Drinks', 'drinks')], max_length=100),
        ),
    ]