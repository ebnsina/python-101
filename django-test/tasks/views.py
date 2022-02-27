from django.shortcuts import render

tasks = [
    { 'id': 1, 'title': 'Task 1'},
    { 'id': 2, 'title': 'Task 2'},
    { 'id': 3, 'title': 'Task 3'},
]

def index(request):
    tasks = []
    return render(request, "tasks/index.html", {'tasks': tasks })

def about(request):
    return render(request, "tasks/about.html")