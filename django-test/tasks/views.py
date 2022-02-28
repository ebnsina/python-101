from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import tasks

from tasks.models import Task
from .forms import TaskForm

# tasks = [
#     { 'id': 1, 'title': 'Task 1'},
#     { 'id': 2, 'title': 'Task 2'},
#     { 'id': 3, 'title': 'Task 3'},
# ]

def index(request):
    tasks = Task.objects.all()
    return render(request, "tasks/index.html", {
        'tasks': tasks
    })

def new_task(request):
    task_form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, "tasks/new.html", {
        'task_form': task_form
    })

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task_form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, "tasks/edit.html", {
        'task_form': task_form
    })


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task.html", {
        'task': task
    })


def task_delete(request, pk):
     task = get_object_or_404(Task, pk=pk)
     task.delete()
     return redirect('index')

def about(request):
    return render(request, "tasks/about.html")