from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import uuid


# Create your models here.

MOVIE_TYPE= (
    ('single', 'Single'),
    ('seasons', 'Seasons')
)


class SubscriptionPlan(models.Model):
     title= models.CharField(max_length=50)
     price = models.DecimalField(max_digits=8, decimal_places=2)
     description = models.TextField() 

     def __str__(self):
        return self.title

class CustomUser(AbstractUser): 
    profiles= models.ManyToManyField('Profile', blank=True, null= True)
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions', blank=True, help_text='Specific permissions for this user.')

    def __str__(self):
        return self.username

class Profile(models.Model):

    username= models.CharField(max_length=20)
    #email= models.EmailField(verbose_name='email address', max_length=255, unique=True)
   # mobile_no= models.CharField(max_length=12, null=True)
   # subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True, blank=True, related_name='profiles')
    uuid= models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.username


class Actors(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movies(models.Model):
    title= models.CharField(max_length=200)
    duration= models.DurationField()
    release_date= models.DateTimeField(auto_now_add=True)
    genres = models.ManyToManyField(Genre)
    actors=models.ManyToManyField(Actors)
    description= models.TextField(null=True)
    uuid= models.UUIDField(default=uuid.uuid4)
    movietype= models.CharField(choices=MOVIE_TYPE, max_length=20, blank=True, null=True)
    video= models.ManyToManyField('Video')
    thumbnailImage= models.ImageField(upload_to='thumbnail',blank=True, null=True)
    

    def __str__(self):
        return self.title


class TVShows(models.Model):
    title= models.CharField(max_length=200)
    seasons=models.IntegerField()
    release_date= models.DateTimeField(auto_now_add=True)
    ratings=models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    genres = models.ManyToManyField(Genre)
    actors=models.ManyToManyField(Actors)
    description= models.TextField(blank=True, null=True)
    uuid= models.UUIDField(default=uuid.uuid4)
    #movietype= models.CharField(choices=MOVIE_TYPE, max_length=20,blank=True, null=True)
    thumbnailImage= models.ImageField(upload_to='thumbnail', blank=True, null=True)

    def __str__(self):
        return self.title



class Episodes(models.Model):
    title= models.CharField(max_length=200)
    duration= models.DurationField()
    aboutEpisode= models.CharField(max_length=500)
    tvShow= models.ForeignKey(TVShows,  on_delete=models.CASCADE, related_name="episodes")
    video= models.ManyToManyField('Video')
    thumbnailImage= models.ImageField(upload_to='thumbnail', blank=True, null=True)
    def __str__(self):
        return self.title
    
class Video(models.Model):
    title= models.CharField(max_length=200)
    file=models.FileField(upload_to='videos')

    def __str__(self):
        return self.title

class MyList(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, null=True, blank=True)
    tv_show = models.ForeignKey(TVShows, on_delete=models.CASCADE, null=True, blank=True)

class ContinueWatching(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, null=True, blank=True)
    tv_show = models.ForeignKey(TVShows, on_delete=models.CASCADE, null=True, blank=True)
    last_watched_time = models.DateTimeField(auto_now=True)





    
 