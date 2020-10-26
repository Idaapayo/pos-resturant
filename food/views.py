from django.shortcuts import render, redirect

# Create your views here.

def food_home(request):
    
    return render(request, 'food.html')

def drinks(request):

    return render(request, 'drinks.html')