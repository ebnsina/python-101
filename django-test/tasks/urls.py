from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/<int:pk>/", views.task_view, name="task"),
    path("new/", views.new_task, name="new"),
    path("tasks/<int:pk>/edit", views.task_edit, name="edit"),
    path("tasks/<int:pk>/delete", views.task_delete, name="delete"),
    path("about/", views.about, name="about"),
]