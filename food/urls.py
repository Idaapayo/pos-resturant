from django.urls import path, re_path
from . import views
from food.views import Sell_page

urlpatterns = [
    path('', views.food_home, name="food_home"),
    path('', Sell_page.as_view() , name='sell_page' ),
    path('drinks', views.drinks, name='drinks')
]