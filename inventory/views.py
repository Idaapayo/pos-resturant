from django.shortcuts import render, redirect
from .forms import ProductsForm, uploadproducts
from django.contrib import messages
import io
import csv
from .models import Products

# Create your views here.




def inventory_home(request):

    product_form = ProductsForm()

    if request.method == 'POST':

        #menu item save form logic
        product_form = ProductsForm(request.POST)
        if product_form.is_valid():
            print("form is valid")
            items = product_form.cleaned_data['items']
            category = product_form.cleaned_data['category']
            subcategory = product_form.cleaned_data['subcategory']
            price = product_form.cleaned_data['price']
            product_form.save()
            messages.success(request, 'Menu item added')
            # redirect('addproducts')
        else:
            product_form = ProductsForm()
    else:
        print("using get")
    context = {'product_form': product_form}
    return render(request, 'inventory.html', context )

def uploadfile(request):
    upload_form = uploadproducts()
    if request.method == 'POST':
        upload_form = uploadproducts(request.POST, request.FILES)

        # upload excelfie form logic
        if upload_form.is_valid():
            csv_file = request.FILES['file_name']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, "This is not a csv file")
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)

            # reading excel columns to db
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                obj, created = Products.objects.update_or_create(
                    items=column[0],
                    category=column[1],
                    subcategory=column[2],
                    price=column[3]
                )
            print("form upload is valid")
            upload_form.save()
            messages.success(request, "file has been uploaded")
        else:
            print("not valid")
    else:
        print("using get")
    context = {'upload_form': upload_form}
    return render(request, 'inventory.html', context)

