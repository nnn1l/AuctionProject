from ninja import Router
from auctions.models.Auction import Auction
from auctions.pydantic import (
    AuctionCreateSchema,
    AuctionUpdateSchema,
    AuctionReadSchema
)

router = Router(tags=["Auctions"])

@router.post("/", response=AuctionReadSchema)
def create_auction(request, data: AuctionCreateSchema):
    auction = Auction.objects.create(
        owner=request.user,
        title=data.title,
        description=data.description,
        end_time=data.end_time,
        start_price=data.start_price,
    )
    return auction

@router.get("/", response=list[AuctionReadSchema])
def list_auctions(request):
    return Auction.objects.all()

@router.patch("/{auction_id}", response=AuctionReadSchema)
def update_auction(request, auction_id: int, data: AuctionUpdateSchema):
    auction = Auction.objects.get(id=auction_id)

    for field, value in data.dict(exclude_unset=True).items():
        setattr(auction, field, value)

    auction.save()
    return auction

