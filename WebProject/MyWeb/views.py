from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

def home(request):
    return render(request, 'home.html')

# MyWeb/views.py
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html')

def beginner(request):
    return render(request, 'beginner.html')

def intermediate(request):
    return render(request, 'intermediate.html')

def professional(request):
    return render(request, 'professional.html')

def expert(request):
    return render(request, 'expert.html')

def start_learning(request):
    return render(request, 'start_learning.html')
# Create your views here.
# functions are HERE