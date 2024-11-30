from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Instructor

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'home.html', {'error': 'Invalid username or password'})

    return render(request, 'home.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')  # New template for logged-in users
    else:
        messages.error(request, "You must be logged in to access the dashboard.")
        return redirect('home')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

# Instructor Roster (Separate Page)
def instructor_roster(request):
    if request.user.is_authenticated:
        instructors = Instructor.objects.all()
        return render(request, 'instructor_roster.html', {'instructors': instructors})
    else:
        messages.error(request, "You must be logged in to view the instructor roster.")
        return redirect('home')

def instructor_details(request, pk):
    if request.user.is_authenticated:
        instructor_details = Instructor.objects.get(id=pk)
        return render(request, 'instructor.html', {'instructor_details': instructor_details})
    else:
        messages.error(request, "You must be logged in to view this page.")
        return redirect('home')