from celery import shared_task
from django.utils import timezone
from auctions.models.Auction import Auction

@shared_task
def end_expired_auctions():
    auctions = Auction.objects.filter(is_active=True, end_time__lte=timezone.now())
    for auction in auctions:
        auction.end_auction()
