from decimal import Decimal
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models.Bid import Bid
from users.models.Wallet import Wallet


@receiver(post_save, sender=Bid)
def handle_new_bid(sender, instance, created, **kwargs):
    if not created:
        return

    auction = instance.auction
    new_bidder = instance.bidder
    amount = instance.amount

    previous_bid = (
        auction.bids
        .exclude(pk=instance.pk)
        .order_by('-amount')
        .first()
    )

    if previous_bid:
        prev_wallet = Wallet.objects.select_for_update().get(
            user=previous_bid.bidder)
        prev_wallet.balance += previous_bid.amount
        prev_wallet.save(update_fields=['balance'])

        previous_bid.delete()

    wallet = Wallet.objects.select_for_update().get(user=new_bidder)
    wallet.balance -= amount
    wallet.save(update_fields=['balance'])

    auction.update_current_price(amount)
