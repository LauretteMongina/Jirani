from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.fields import related
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    photo = CloudinaryField('image')
    description = models.TextField()
    occupants_count= models.IntegerField( default=0, blank=True)
    health_toll =  models.IntegerField(null=True, blank=True)
    police_toll =  models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = CloudinaryField('image')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    email = models.EmailField(blank=True, max_length=120)
    location = models.CharField(max_length=30, blank=True, null=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, related_name='neighbours', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()




class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()
class Post(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField(max_length=255)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='posting')
    user = user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='developer')