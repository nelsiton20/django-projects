from django.shortcuts import redirect, render

from django.contrib.auth import login
from django.contrib.auth import logout

from django.contrib import messages
from .forms import RegisterUser
from .forms import Login

from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = Login(data=request.POST or None) 
    
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user() # este método devuelve el usuario logueado
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectas')
    
    return render(request, 'user/login.html', {
        'form': form
    })
    
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = RegisterUser(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        user = form.save()  
        login(request, user)
        return redirect('home')
    
    return render(request, 'user/register.html', {
        'form': form
    })
    
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')