from typing import Optional

from pydantic import BaseModel


class ItemBaseSchema(BaseModel):
    title: str
    description: str
    category_id: int


class ItemCreateSchema(ItemBaseSchema):
    pass


class ItemUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None


class ItemReadSchema(ItemBaseSchema):
    id: int
    owner_id: int
    auction_id: Optional[int]

    class Config:
        from_attributes = True
