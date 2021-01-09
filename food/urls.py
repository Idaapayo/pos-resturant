from django.urls import path, re_path
from . import views
from food.views import Subcateg_list

urlpatterns = [
    # path('', views.food_home, name="food_home"),
    path('', Subcateg_list.as_view(), name='subcateg_list_url'),
    path('drinks', views.drinks, name='drinks')
]