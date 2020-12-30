from django.forms import ModelForm, Textarea
from .models import Products, Csv
from django import forms
import io
import csv
from betterforms.multiform import MultiModelForm

# class Multipleform(forms.Form):
#     action = forms.CharField(max_length=60, widget=forms.HiddenInput())



class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        widgets = {'price': forms.TextInput()}

class Uploadproducts(ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)










