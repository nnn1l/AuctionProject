from django.shortcuts import render

from ..models import Auction


def auction_list(request):
    template_name = 'all-auctions.html'
    all_auctions = Auction.objects.prefetch_related('items')
    return render(request, "all-auctions.html", {"auctions": all_auctions})

