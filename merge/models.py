from django.db import models
from ucontent.models import User_content
from pcontent.models import Peer_content
# Create your models here.

#put all info together 
class Content (models.Model):
    user_post = models.ForeignKey(User_content, blank=False, on_delete=models.CASCADE, related_name='contents')
    peer_post = models.ManyToManyField(Peer_content, blank=True)
    card = models.BooleanField(default=False)

    def __str__ (self):
        return str(self.card)
