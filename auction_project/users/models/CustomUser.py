from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='user-avatars', blank=True, null=True)
    biography = models.TextField(max_length=300, blank=True, null=True)
    last_info_changed = models.DateField(auto_now=True)
    auction_wins = models.IntegerField(default=0)
    auction_hosted = models.IntegerField(default=0)

    def __str__(self):
        return self.username