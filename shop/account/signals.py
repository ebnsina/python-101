from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User, Customer


@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
    
        

@receiver(post_save, sender=Customer)
def update_customer(sender, instance, created, **kwargs):
    if not created:
        customer = instance
        user = customer.user
        user.name = customer.name
        user.save()
    


@receiver(post_delete, sender=Customer)
def delete_customer(sender, instance, created, **kwargs):
    user = instance.user
    user.delete()
    