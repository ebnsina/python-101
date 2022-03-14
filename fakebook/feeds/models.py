from django.db import models
from account.models import Profile



class Feed(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="feeds/", null=True, blank="True")
    posted_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank="True")


    def __str__(self):
        return self.title



class Comment(models.Model):
    body = models.TextField()
    feed = models.ForeignKey(
        Feed,  on_delete=models.CASCADE, null=True, blank="True")
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank="True")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
