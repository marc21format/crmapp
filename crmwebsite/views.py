from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from .forms import SignUpForm, AddInstructorForm
from .models import Instructor
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

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

from django.shortcuts import render
from django.db.models import Q
from .models import Instructor

def instructor_roster(request):
    query = request.GET.get('search', '')
    filter_by = request.GET.get('filter', 'all')  # Default to 'all' if no filter is selected

    if filter_by == 'all' and query:
        instructors = Instructor.objects.filter(
            first_name__icontains=query) | Instructor.objects.filter(
            middle_name__icontains=query) | Instructor.objects.filter(
            last_name__icontains=query) | Instructor.objects.filter(
            honorary_title__icontains=query) | Instructor.objects.filter(
            suffix__icontains=query) | Instructor.objects.filter(
            batch__icontains=query) | Instructor.objects.filter(
            undergrad_course__icontains=query) | Instructor.objects.filter(
            undergrad_school__icontains=query) | Instructor.objects.filter(
            undergrad_award__icontains=query) | Instructor.objects.filter(
            undergrad_scholarship__icontains=query) | Instructor.objects.filter(
            postgrad_course__icontains=query) | Instructor.objects.filter(
            postgrad_school__icontains=query) | Instructor.objects.filter(
            postgrad_award__icontains=query) | Instructor.objects.filter(
            postgrad_scholarship__icontains=query) | Instructor.objects.filter(
            other_achievments__icontains=query) | Instructor.objects.filter(
            status__icontains=query) | Instructor.objects.filter(
            email__icontains=query)
    
    elif filter_by == 'first_name' and query:
        instructors = Instructor.objects.filter(first_name__icontains=query)
    elif filter_by == 'middle_name' and query:
        instructors = Instructor.objects.filter(middle_name__icontains=query)
    elif filter_by == 'last_name' and query:
        instructors = Instructor.objects.filter(last_name__icontains=query)
    elif filter_by == 'honorary_title' and query:
        instructors = Instructor.objects.filter(honorary_title__icontains=query)
    elif filter_by == 'suffix' and query:
        instructors = Instructor.objects.filter(suffix__icontains=query)
    elif filter_by == 'batch' and query:
        instructors = Instructor.objects.filter(batch__icontains=query)
    elif filter_by == 'undergrad_course' and query:
        instructors = Instructor.objects.filter(undergrad_course__icontains=query)
    elif filter_by == 'undergrad_school' and query:
        instructors = Instructor.objects.filter(undergrad_school__icontains=query)
    elif filter_by == 'undergrad_award' and query:
        instructors = Instructor.objects.filter(undergrad_award__icontains=query)
    elif filter_by == 'undergrad_scholarship' and query:
        instructors = Instructor.objects.filter(undergrad_scholarship__icontains=query)
    elif filter_by == 'postgrad_course' and query:
        instructors = Instructor.objects.filter(postgrad_course__icontains=query)
    elif filter_by == 'postgrad_school' and query:
        instructors = Instructor.objects.filter(postgrad_school__icontains=query)
    elif filter_by == 'postgrad_award' and query:
        instructors = Instructor.objects.filter(postgrad_award__icontains=query)
    elif filter_by == 'postgrad_scholarship' and query:
        instructors = Instructor.objects.filter(postgrad_scholarship__icontains=query)
    elif filter_by == 'other_achievments' and query:
        instructors = Instructor.objects.filter(other_achievments__icontains=query)
    elif filter_by == 'status' and query:
        instructors = Instructor.objects.filter(status__icontains=query)
    elif filter_by == 'email' and query:
        instructors = Instructor.objects.filter(email__icontains=query)
    else:
        instructors = Instructor.objects.all()

    return render(request, 'instructor_roster.html', {
        'instructors': instructors,
        'query': query,
        'filter': filter_by,
    })

def instructor_details(request, pk):
    if request.user.is_authenticated:
        instructor_details = Instructor.objects.get(id=pk)
        instructor_details.last_updated = timezone.localtime(instructor_details.last_updated)
        return render(request, 'instructor.html', {'instructor_details': instructor_details})
    else:
        messages.error(request, "You must be logged in to view this page.")
        return redirect('home')

def delete_instructor(request, pk):
    if request.user.is_authenticated:
        delete_it = Instructor.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Instructor Deleted Successfully")
        return redirect('instructor_roster')
    else:
        messages.success(request, "You Must Be Logged In To Do That")
        return redirect('home')

def add_instructor(request):
    if request.method == 'POST':
        form = AddInstructorForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Instructor Has Been Added Successfully.")
            return redirect('instructor_roster')  # Redirect after successful submission
    else:
        form = AddInstructorForm()

    return render(request, 'add_instructor.html', {'form': form})

def update_instructor(request, pk):
    if request.user.is_authenticated:
        current_instructor = Instructor.objects.get(id=pk)
        form = AddInstructorForm(request.POST or None, instance=current_instructor)

        if form.is_valid():
            instructor = form.save(commit=False)  # Don't commit to DB yet
            instructor.updated_by = request.user  # Set updated_by to the current logged-in user
            instructor.save()  # Save the updated instructor
            messages.success(request, "Instructor Has Been Updated Successfully.")
            return redirect('instructor_roster')
        
        return render(request, 'update_instructor.html', {'form': form})
    else:
        messages.error(request, "You Must Be Logged In To Do That")
        return redirect('home')

def confirm_delete_instructor(request, pk):
    instructor = get_object_or_404(Instructor, id=pk)
    
    if request.method == 'POST':
        instructor.delete()
        messages.success(request, "Instructor Deleted Successfully")
        return redirect('instructor_roster')  # Redirect to the instructor list page
    
    return render(request, 'confirm_delete_instructor.html', {'instructor': instructor})