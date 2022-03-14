from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        Profile.objects.create(user=user)


@receiver(post_save, sender=Profile)
def update_profile(sender, instance, created, **kwargs):
    print(instance, created)
    profile = instance
    user = profile.user

    if not created:
        user.name = profile.name
        user.save()


@receiver(post_delete, sender=Profile)
def delete_profile(sender, instance, **kwargs):
    user = instance.user
    user.delete()
