from tkinter import E
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomRegisterFrom

def register_view(request):
    form = CustomRegisterFrom()

    if request.method == 'POST':
        form = CustomRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect("login")
            
    return render(request, "account/register.html", {
        "form": form
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials.")
            
    return render(request, "account/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
