from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from decimal import Decimal


class AuctionBaseSchema(BaseModel):
    title: str
    description: str = ''
    end_time: datetime
    start_price: Decimal


class AuctionCreateSchema(AuctionBaseSchema):
    pass


class AuctionUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    end_time: Optional[datetime] = None


class AuctionReadSchema(AuctionBaseSchema):
    id: int
    start_time: datetime
    owner_id: int

    class Config:
        from_attributes = True


class BidIn(BaseModel):
    auction_id: int
    amount: Decimal


class BidOut(BaseModel):
    id: int
    amount: Decimal
    bidder_id: int

    class Config:
        from_attributes = True
