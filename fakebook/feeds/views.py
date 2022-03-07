from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Feed
from .forms import FeedForm

def index(request):
    feeds = Feed.objects.all()
    return render(request, "feeds/index.html", {
        'feeds': feeds
    })



def new_post(request):
    form = FeedForm()

    if request.method == 'POST':
        form = FeedForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Post created successfully.")
            return redirect('index')

    return render(request, "feeds/form.html", {
        'form': form
    })
