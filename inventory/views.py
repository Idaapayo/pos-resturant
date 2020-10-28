from django.shortcuts import render, redirect
from .forms import addproducts_form

# Create your views here.

def inventory_home(request):
    return render(request, 'inventory.html')

def addproducts(request):
    if request.method == 'POST':
        addprod_form = addproducts_form(request.POST)
        if addprod_form.is_valid():
            items = addprod_form.cleaned_data['items']
            categories = addprod_form.cleaned_data['categories']
            subcategory = addprod_form.cleaned_data['subcategory']
            price = addprod_form.cleaned_data['price']
    return