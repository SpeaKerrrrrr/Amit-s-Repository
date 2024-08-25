from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

# Home view
def home(request):
    return render(request, 'home.html')

# Registration view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to a profile page or home
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log in the user
            return redirect('home')  # Redirect to the profile page or another page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Profile view
def profile(request):
    return render(request, 'profile.html')

# About view
def about(request):
    return render(request, 'about.html')

# Experience level views
def beginner(request):
    return render(request, 'beginner.html')

def intermediate(request):
    return render(request, 'intermediate.html')

def professional(request):
    return render(request, 'professional.html')

def expert(request):
    return render(request, 'expert.html')

# Start Learning view
def start_learning(request):
    return render(request, 'start_learning.html')

def beginner_questions(request):
    return render(request, 'beginner_questions.html')
    