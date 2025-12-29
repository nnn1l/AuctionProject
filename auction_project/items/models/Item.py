from django.db import models
from .Category import Category
from users.models.CustomUser import CustomUser # ignore errors with import, it works
from auctions.models.Auction import Auction
from django.utils.translation import gettext_lazy as _

class Item(models.Model):
    title = models.CharField(
        max_length=40,
        default='Title',
        verbose_name=_('Title')    #  <-- '_' is gettext_lazy()
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=False,
        verbose_name=_('Category')
    )

    image = models.ImageField(
        upload_to='item-images/',
        blank=True,
        default='default_images/default_item_image.png',
        verbose_name=_('Image')
    )

    description = models.TextField(
        max_length=1000,
        blank=True,
        default='',
        verbose_name=_('Description')
    )

    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        default=1,
        related_name='items',
        verbose_name=_('Owner')
    )

    auction = models.ForeignKey(
        Auction,
        on_delete=models.SET_NULL,
        related_name='items',
        null=True,
        blank=True,
        verbose_name=_('Auction')
    )


    def __str__(self):
        return self.title