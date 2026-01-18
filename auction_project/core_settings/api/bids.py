from ninja import Router
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from auctions.models.Auction import Auction  # ignore ide errors
from auctions.models.Bid import Bid
from auctions.pydantic import BidIn, BidOut

router = Router(tags=["Bids"])

@router.post("/", response=BidOut)
@login_required
def place_bid(request, data: BidIn):
    auction = get_object_or_404(Auction, id=data.auction_id)
    user = request.user

    if not user.wallet.can_afford(data.amount):
        return 400, {"detail": "Insufficient funds"}

    try:
        auction.update_current_price(data.amount)

        bid = Bid.objects.create(
            auction=auction,
            bidder=user,
            amount=data.amount
        )

    except ValueError as e:
        return 400, {"detail": str(e)}

    return bid


@router.get("/auction/{auction_id}", response=list[BidOut])
def auction_bids(request, auction_id: int):
    return Bid.objects.filter(
        auction_id=auction_id
    ).select_related("bidder")


@router.get("/my", response=list[BidOut])
@login_required
def my_bids(request):
    return Bid.objects.filter(
        bidder=request.user
    ).select_related("auction")


@router.get("/{bid_id}", response=BidOut)
def get_bid(request, bid_id: int):
    return get_object_or_404(Bid, id=bid_id)
