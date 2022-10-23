
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile



#Create a profile for each User
#this create a profile anytime a user creates a profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


#This save the profile when the user is save
@receiver(post_save, sender=User)
def save_profile(sender,instance, **kwargs):
    instance.profile.save()




#signals is imported in the apps.py file