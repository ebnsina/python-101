from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomRegisterFrom, ProfileForm

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


@login_required(login_url='login')
def profile(request):
    profile = request.user.profile

    return render(request, 'account/profile.html', {
        'profile': profile
    })

@login_required(login_url='login')
def profile_update(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('index')

    return render(request, 'account/profile-update.html', {
        'profile': profile,
        'form': form
    })
