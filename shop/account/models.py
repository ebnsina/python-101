from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='avatar/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user)
