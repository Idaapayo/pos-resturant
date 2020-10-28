from django import forms


category_choices =  (
    ('Food', 'food'),
    ('Drinks', "drinks")
)

class addproducts_form(forms.Form):
    items = forms.CharField(max_length=100)
    categories = forms.ChoiceField(choices=category_choices)
    subcategory = forms.CharField(max_length=100)
    price = forms.FloatField(max_length=100)
