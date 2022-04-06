from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignupForm



def signup(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sign Up successfully.')
            return redirect('signin')


    return render(request, 'account/signup.html', {
        'form': form
    })


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully.')
            return redirect('index')
        else:
            messages.error(request, 'Wrong credentials')
        
    return render(request, 'account/signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'Logout successfully.')
    return redirect('signin')
