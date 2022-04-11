from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignupForm, CustomerForm



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

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Wrong credentials')

    return render(request, 'account/signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'Logout successfully.')
    return redirect('signin')



def account(request):
     customer = request.user.customer
     return render(request, 'account/account.html', {
          'customer': customer
     })


def account_update(request):
    form = CustomerForm()
    customer = request.user.customer

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated.')

    return render(request, 'account/update-account.html', {
            'form': form,
            'customer': customer
    })









