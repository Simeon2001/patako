from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#main content 
class User_content (models.Model):
    name = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name='lives')
    title = models.CharField(max_length=50, blank=True)
    post = models.TextField(max_length=300, blank=False)
    peer_limit = models.IntegerField(default=0)

    def __str__ (self):
        return self.title