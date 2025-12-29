from django.db import models, transaction
from decimal import Decimal
from .Auction import Auction
from users.models.CustomUser import CustomUser
from users.models.Wallet import Wallet
from django.utils.translation import gettext_lazy as _


class Bid(models.Model):
    auction = models.ForeignKey(
        Auction,
        on_delete=models.CASCADE,
        related_name='bids',
        verbose_name=_('Auction')    #  <-- '_' is gettext_lazy()
    )

    bidder = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='bids',
        verbose_name=_('Bidder')
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Amount')
    )

    def save(self, *args, **kwargs):
        if self.amount <= self.auction.current_price:
            raise ValueError("Bid must be higher than current price")
        super().save(*args, **kwargs)