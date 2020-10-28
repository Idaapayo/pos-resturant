from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_home , name='inventory_home' ),
    path("addproducts", views.addproducts, name='addproducts')

]