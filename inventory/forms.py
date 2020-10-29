from django.forms import ModelForm, Textarea
from .models import Products, Csv
from django import forms

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        # widgets = {'items': Textarea(attrs={})}





