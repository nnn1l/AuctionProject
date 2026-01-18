from datetime import datetime
from decimal import Decimal
from typing import Optional, Literal

from pydantic import BaseModel


class UserReadSchema(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    avatar: str
    biography: str
    auction_wins: int
    auction_hosted: int

    class Config:
        from_attributes = True


class UserUpdateSchema(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    biography: Optional[str] = None


class WalletOut(BaseModel):
    balance: Decimal


class WalletDepositIn(BaseModel):
    amount: Decimal


class WalletWithdrawIn(BaseModel):
    amount: Decimal


class WalletTransactionOut(BaseModel):
    id: int
    amount: Decimal
    type: Literal["deposit", "withdraw", "bid_hold", "refund"]
    created_at: datetime


