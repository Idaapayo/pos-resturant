from django.forms import ModelForm, Textarea
from .models import Products, Csv
from django import forms
import io
import csv


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        widgets = {'price': forms.TextInput()}

class uploadproducts(ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)

    def process_data():
        """fun to add csv column data into database"""

        # file = io.TextIOWrapper(cleaned_data['file_name'].file)
        # reader = csv.DictReader(file)
        #
        # for product in reader:
        #     Products.objects.get_or_create(
        #         items=product[0],
        #         category=product[1],
        #         subcategory=product[2],
        #         price = product[3]
        #     )








