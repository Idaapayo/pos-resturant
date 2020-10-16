from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Credentials
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required, user_passes_test
from .decorators import unauthenticated_user, allowed_users


from django.http import HttpResponse

# Create your views here.

@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('login_logic')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required(login_url = 'login')
def login_logic(request):
    return render(request, 'index_page.html')

@allowed_users(allowed_roles=['admins'])
def test(request):
    return render(request, 'test.html')

@unauthenticated_user
def registration(request):
    if request.method == 'POST':
       first_name = request.POST['firstname']
       last_name = request.POST['lastname']
       username = request.POST['usernamesignup']
       email = request.POST['emailsignup']
       password1 = request.POST['passwordsignup1']
       password2 = request.POST['passwordsignup2']
       if password1 == password2:
           if User.objects.filter(username=username).exists():
               messages.info(request, 'Username Taken')
               return redirect('registration')
           elif User.objects.filter(email=email).exists():
               messages.info(request, 'Email Taken')
               return redirect('registration')
           else:
               user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
               user.save()
               print('user created')
               return redirect('login')
       else:
           messages.info(request, 'Password is not matching')
           return redirect('registration')
       return redirect('registration')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')