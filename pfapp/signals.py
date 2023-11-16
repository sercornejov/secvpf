from django.contrib.auth.models import User,Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Geninfo

@receiver(post_save, sender=Geninfo)

def addUser_usuexterno_group(sender,instance,created,**kwargs):
  if created:
    try:
      usuexternos=Group.objects.get(name='usuexterno')
    except Group.DoesNotExist:
      usuexternos=Group.objects.create(name='usuexterno')
    instance.user.groups.add(usuexternos)