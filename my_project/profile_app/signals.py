from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from profile_app.models import Profile


@receiver(post_save, sender=Profile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_delete, sender=Profile)
def post_delete(sender, instance, **kwargs):
    instance.profile.delete()
