from django.shortcuts import render, redirect

from .forms import RegisterUser, Login

from publications.models import Publication
from publications.forms import ComentForm

from django.contrib.auth import login
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

def index(request):
    publications = Publication.objects.all()
    form = ComentForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        pass
    
    return render(request, 'index.html', {'publications':publications, 'form' : form})

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    form = RegisterUser(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('index')
    
    return render(request, 'register.html', {'form':form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    form = Login(data=request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('index')
    
    return render(request, 'login.html', {'form':form})

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('index')