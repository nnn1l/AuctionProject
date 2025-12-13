from datetime import timedelta
from django.utils import timezone
from django.db import models
from users.models.CustomUser import CustomUser # ignore errors with import, it works


#def default_end_time():
    #return timezone.now() + timedelta(days=1)

class Auction(models.Model):
    title = models.CharField(max_length=40, null=False, default='Title')
    description = models.TextField(max_length=1000, blank=True, default='')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=False)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1, related_name='auctions')
    start_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)

    def __str__(self):
        return self.title