from django.db import models
from .Category import Category
from users.models.CustomUser import CustomUser # ignore errors with import, it works
from auctions.models.Auction import Auction

class Item(models.Model):
    title = models.CharField(max_length=40, default='Title')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to='item-images/', blank=True, default='default_images/default_item_image.png')
    description = models.TextField(max_length=1000, blank=True, default='')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1, related_name='items')
    auction = models.ForeignKey(Auction,on_delete=models.SET_NULL, related_name='items', null=True,
                                blank=True)

    def __str__(self):
        return self.title