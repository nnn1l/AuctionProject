from django.db import models
from .Category import Category
from users.models.CustomUser import CustomUser # ignore errors with import, it works
from auctions.models.Auction import Auction

class Item(models.Model):
    title = models.CharField(max_length=40, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item-images/')
    description = models.TextField(max_length=1000, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=4, related_name='items')
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='items', null=True,
                                blank=True)

    def __str__(self):
        return self.title