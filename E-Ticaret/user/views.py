from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
# from django.core.mail import send_mail
# from django.conf import settings

from user.forms import UserForm

# Create your views here.

def userRegister(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # subject = 'Güvenli Alışveriş Hesap Oluşturma'
            # message = 'Güvenli Alışveriş hesabınız başarılı bir şekilde oluşturulmuştur. Keyifli alışverişler dileriz :)'
            # send_mail(
            #     subject,
            #     message,
            #     settings.EMAIL_HOST_USER,
            #     [form.email],
            #     fail_silently = False
            # )
            form.save()
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print("Kullanıcı adı veya şifre hatalı")
            return redirect('login')
    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    return redirect('index')