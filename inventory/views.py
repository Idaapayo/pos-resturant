from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductsForm, Uploadproducts
from django.contrib import messages
import io
import csv
from .models import Products
from multi_form_view import MultiFormView, MultiModelFormView
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin, CreateView
from django.http import HttpResponseForbidden



class Inventory_view(MultiModelFormView):
    template_name = 'inventory.html'
    form_classes = {
        'product_form': ProductsForm,
        'upload_form': Uploadproducts
    }
    success_url = reverse_lazy("inventory_home")


    def post(self, request, *args, **kwargs):

        # action = self.request.POST.get('action')
        # action1 = self.request.POST.get('action1')
        # print(action)
        # if action == 'product_form':
        print("submiting prod_form")
        product_form = ProductsForm(request.POST)
        self.product_form(product_form, request)

        # if action == 'upload_form':
        print("submiting upload_form")
        upload_form = Uploadproducts(request.POST, request.FILES)
        self.upload_csv(upload_form, request)
        return super().post(request, **kwargs)


    def product_form(self, form_name, request):
        """
        fun to process the ProductsForm to store a menu item
        :param form_name:
        :param form_classes:
        :return:
        """
        product_form = form_name

        if not product_form:
            return HttpResponseForbidden()
        elif product_form.is_valid():
            print("form is valid")
            items = product_form.cleaned_data['items']
            category = product_form.cleaned_data['category']
            subcategory = product_form.cleaned_data['subcategory']
            price = product_form.cleaned_data['price']
            product_form.save()
            messages.success(request, "menu item added")
        else:
            return self.form_invalid(product_form)

    def upload_csv(self, form_name, request):

        print("in upload form")
        upload_form = form_name

        if upload_form.is_valid():
            print("form is val")
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
            upload_form.save()
            messages.success(request, "file has been uploaded")
        else:
            return self.form_invalid(upload_form)


