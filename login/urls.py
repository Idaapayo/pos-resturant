from django.urls import path
from . import views

urlpatterns = [

    path('login',views.login , name='login'),
    path('login_logic', views.login_logic, name = "login_logic"),
    path('registration', views.registration, name = "registration"),
    path('logout', views.logout, name= 'logout'),
    path('test', views.test, name='test')
]
