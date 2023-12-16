from django.db.models.signals import post_save
from blog.models import custom_user
import uuid
from django.dispatch import receiver
from.models import profile
@receiver(post_save,sender=custom_user)
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save,sender=custom_user)
def save_profile(sender, instance , **kwargs):
        instance.profile.save()
random=uuid.uuid4()
