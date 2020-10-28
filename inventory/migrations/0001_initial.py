# Generated by Django 2.2.7 on 2020-10-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='excelFiles')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Food', 'food'), ('Drinks', 'drinks')], max_length=100)),
                ('subcategory', models.CharField(max_length=100)),
                ('price', models.FloatField(max_length=100)),
            ],
        ),
    ]