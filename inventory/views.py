from django.shortcuts import render, redirect
from .forms import ProductsForm

# Create your views here.

def inventory_home(request):
    product_form = ProductsForm()
    context = {'product_form': product_form}
    if request.method == 'POST':
        product_form = ProductsForm(request.POST)
        if product_form.is_valid():
            # items = product_form.cleaned_data['items']
            # categories = product_form.cleaned_data['categories']
            # subcategory = product_form.cleaned_data['subcategory']
            # price = product_form.cleaned_data['price']
            product_form.save()
            # redirect('addproducts')
        else:
            product_form = ProductsForm()
    return render(request, 'inventory.html', context)

# def addproducts(request):
#
#
#     return render(request, 'inventory.html', context)