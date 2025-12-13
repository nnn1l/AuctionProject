from typing import Optional

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
