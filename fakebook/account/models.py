from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    bio = models.TextField(max_length=500)
    profile_photo = models.ImageField(
        upload_to="profile_photo/", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
