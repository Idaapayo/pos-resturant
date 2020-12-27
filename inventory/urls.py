from django.urls import path, re_path
from . import views
from inventory.views import Inventory_view

urlpatterns = [
    re_path(r'^$', Inventory_view.as_view(), name='inventory_home'),

]