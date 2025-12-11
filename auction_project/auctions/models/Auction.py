from django.db import models
from users.models.CustomUser import CustomUser # ignore errors with import, it works

class Auction(models.Model):
    title = models.CharField(max_length=40, null=True)
    description = models.TextField(max_length=1000, null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=4, related_name='auctions')
    start_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.title