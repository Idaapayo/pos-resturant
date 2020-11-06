from django.contrib import admin
from .models import Csv, Products
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

admin.site.register(Csv)
admin.site.register(Products)

# class ProductsResorce(resources.ModelResource):
#     class Meta:
#         model = Products
