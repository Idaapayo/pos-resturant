from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from inventory.models import Products
# Create your views here.

class Subcateg_list(ListView):
   model = Products
   template_name = "food.html"
   context_object_name = "subcateg_list"

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # context['food_items_qr'] = Products.objects.all()
       # print(context)
       return context

   def get_queryset(self):
       qr = Products.objects.order_by().values('subcategory').distinct()
       # qr = Products.objects.all()
       print('qr retrieved')
       return qr


# def food_home(request):
#     return render(request, 'food.html')

def drinks(request):
    return render(request, 'drinks.html')