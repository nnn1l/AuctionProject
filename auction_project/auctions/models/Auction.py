from datetime import timedelta
from decimal import Decimal
from django.utils.translation import gettext_lazy as _

from django.utils import timezone
from django.db import models
from users.models.CustomUser import CustomUser # ignore errors with import, it works


#def default_end_time():
    #return timezone.now() + timedelta(days=1)

class Auction(models.Model):
    title = models.CharField(
        max_length=40,
        null=False,
        default='Title',
        verbose_name=_('Title')    #  <-- '_' is gettext_lazy()
    )

    description = models.TextField(
        max_length=1000,
        blank=True,
        default='',
        verbose_name=_('Description')
    )

    start_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Start Time')
    )

    end_time = models.DateTimeField(
        blank=False,
        verbose_name=_('End Time')
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Is Active')
    )

    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        default=1,
        related_name='auctions',
        verbose_name=_('Owner')
    )

    start_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('Start Price')
    )

    current_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name=_('Current Price')
    )


    def __str__(self):
        return self.title

    def update_current_price(self, amount):
        """  Updates price of auction  """

        if not isinstance(amount, Decimal):
            amount = Decimal(str(amount))

        if amount > self.current_price:
            self.current_price = amount
            self.save(update_fields=['current_price'])


    def attach_items(self, items):
        items.update(auction=self)


    def end_auction(self):
        """  Ends auction with its winning logic  """

        if not self.is_active:
            return

        self.is_active = False
        self.save(update_fields=['is_active'])

        winning_bid = self.bids.order_by('-amount').first()
        if not winning_bid:
            self.items.update(auction=None)
            return

        owner_wallet = self.owner.wallet
        owner_wallet.balance += winning_bid.amount
        owner_wallet.save()

        winner = winning_bid.bidder

        winner.auction_wins =+ 1
        self.owner.auction_hosted =+ 1

        self.items.update(owner=winner, auction=None)