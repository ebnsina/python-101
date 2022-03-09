from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post/", views.new_post, name="post"),
    path("posts/<int:pk>/", views.single_post, name="single-post"),
    path("posts/<int:pk>/edit", views.edit_post, name="edit-post"),
    path("posts/<int:pk>/delete", views.delete_post, name="delete-post"),
]
