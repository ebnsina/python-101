from django.db import models

class Feed(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="feeds/", null=True, blank="True")
    posted_at = models.DateTimeField(auto_now_add=True)