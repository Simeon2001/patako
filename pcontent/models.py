from django.db import models
from ucontent.models import User_content
# Create your models here.

#peers writeup 
class Peer_content (models.Model):
    ucontent = models.ForeignKey(User_content, blank=False, on_delete=models.CASCADE, related_name='peers')
    title = models.CharField(max_length=50, blank=True)
    peer_name = models.CharField(max_length=50, blank=False)
    mail = models.EmailField(blank=True)
    post = models.TextField(max_length=300, blank=False)
    add_merge = models.BooleanField(default=False)
    limit = models.IntegerField(default=0)

    def __str__ (self):
        return self.title