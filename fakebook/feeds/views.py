from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Feed, Comment
from .forms import FeedForm, CommentForm


def index(request):
    feeds = Feed.objects.order_by('-posted_at')
    return render(request, "feeds/index.html", {
        'feeds': feeds
    })


@login_required(login_url='login')
def new_post(request):
    form = FeedForm()

    if request.method == 'POST':
        form = FeedForm(request.POST, request.FILES)

        if form.is_valid():
            feed = form.save(commit=False)
            feed.posted_by = request.user.profile
            feed.save()

            messages.success(request, "Post created successfully.")
            return redirect('index')

    return render(request, "feeds/form.html", {
        'form': form,
    })


def single_post(request, pk):
    form = CommentForm()
    feed = get_object_or_404(Feed, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
           comment = form.save(commit=False)
           comment.feed = feed
           comment.author = request.user.profile
           comment.save()
           messages.success(request, "Comment added successfully.")

    return render(request, "feeds/post.html", {
        'feed': feed,
        'form': form,
    })



@login_required(login_url='login')
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


@login_required(login_url='login')
def delete_post(request, pk):
    feed = get_object_or_404(Feed, pk=pk)
    feed.delete()
    messages.success(request, "Post deleted successfully.")
