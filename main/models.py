from django.db import models
from django.contrib.auth.models import User
from merge.models import Content

# Create your models here.

#profile models
class Profile (models.Model):
    user = models.OneToOneField(User, blank=False, on_delete=models.CASCADE,related_name='profiles')
    avatar = models.CharField(max_length=100, blank=True)
    interest = models.CharField(max_length=30, blank=False)
    
    def __str__ (self):
        return self.interest

#main post models
class Post (models.Model):
    profile = models.ForeignKey(Profile, blank=False, on_delete=models.CASCADE, related_name='posts')
    content = models.ForeignKey(Content, blank=False, on_delete=models.CASCADE, default=1)
    push = models.BooleanField(default=True)
    tag = models.CharField(max_length=30, blank=True)
    click = models.IntegerField(blank=True, default=0)

    def __str__ (self):
        return self.tag
