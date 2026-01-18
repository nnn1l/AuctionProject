from ninja import Router
from items.models.Item import Item  #ignore IDE errors
from items.pydantic import ItemCreateSchema, ItemUpdateSchema, ItemReadSchema

router = Router(tags=["Items"])


@router.post("/", response=ItemReadSchema)
def create_item(request, data: ItemCreateSchema):
    item = Item.objects.create(
        owner=request.user,
        title=data.title,
        description=data.description,
        category_id=data.category_id,
    )
    return item

@router.get("/", response=list[ItemReadSchema])
def list_items(request):
    return Item.objects.all()

@router.patch("/{item_id}", response=ItemReadSchema)
def update_item(request, item_id: int, data: ItemUpdateSchema):
    item = Item.objects.get(id=item_id)

    for field, value in data.dict(exclude_unset=True).items():
        setattr(item, field, value)

    item.save()
    return item

