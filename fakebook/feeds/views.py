from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Feed
from .forms import FeedForm

def index(request):
    feeds = Feed.objects.order_by('-posted_at')
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
        'form': form,
    })


def single_post(request, pk):
    feed = get_object_or_404(Feed, pk=pk)
    return render(request, "feeds/post.html", {
        'feed': feed
    })


def edit_post(request, pk):
    feed = get_object_or_404(Feed, pk=pk)
    form = FeedForm(instance=feed)

    if request.method == 'POST':
        form = FeedForm(request.POST, request.FILES, instance=feed)

        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect('index')

    return render(request, "feeds/form.html", {
        'feed': feed,
        'form': form
    })


def delete_post(request, pk):
    feed = get_object_or_404(Feed, pk=pk)
    feed.delete()
    messages.success(request, "Post deleted successfully.")
