from django.db import models
from items.models.Item import Item # ignore errors with import, it works

class Auction(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)