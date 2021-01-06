from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from inventory.models import Products
# Create your views here.

class Sell_page(ListView):
   model = Products
   template_name = "food.html"

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       return context


def food_home(request):
    return render(request, 'food.html')

def drinks(request):
    return render(request, 'drinks.html')