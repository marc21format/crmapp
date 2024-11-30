from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Instructor

def home(request):
	instructors = Instructor.objects.all()



	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged login")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In.")
			return redirect('home')

	else:
		return render(request, 'home.html', {'instructors':instructors})

def logout_user(request):
		logout(request)
		messages.success(request, "You Have Been Logged Out...")
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
			messages.success(request, "You Have Successfully Registered!")	
			return redirect('home')

	else:
			form= SignUpForm()
			return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



def instructor_roster(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		instructor_roster = Instructor.objects.get(id=pk)
		return render(request, 'instructor.html', {'instructor_roster':instructor_roster})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')