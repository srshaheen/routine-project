from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import RoutineForm
from .models import Course, Routine


# home page function
@login_required(login_url='login')
def DashBoard(request):
    if request.method == 'POST':
        department = request.POST.get('department')
        all_routine = Routine.objects.filter(department=department)
        return render(request, 'routineapp/dashboard.html', {'routine': all_routine})

    all_routine = Routine.objects.all()
    return render(request, 'routineapp/dashboard.html', {'routine': all_routine})


#all course fucntion  
def AllCourses(request):
    if request.method == 'POST':
        department = request.POST.get('department')
        all_courses = Course.objects.filter(department=department)
        return render(request, 'routineapp/all-classes.html', {'course': all_courses})

    all_courses = Course.objects.all()
    return render(request, 'routineapp/all-classes.html', {'course': all_courses})


# signup function
def SignUp(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return render(request, 'routineapp/signup.html', {'alert': 'Your Password and confirm password is not same'})
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        return redirect(LogIn)
    return render(request, 'routineapp/signup.html')


# login function
def LogIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect(DashBoard)
        else:
            return render(request, 'routineapp/login.html', {'message': 'Incorrect Password or Username'})

    return render(request, 'routineapp/login.html')


# logout function
def LogOut(request):
    logout(request)
    return redirect(LogIn)



