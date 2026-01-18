from ninja import Router
from django.contrib.auth import get_user_model
from users.pydantic import UserReadSchema, UserUpdateSchema

User = get_user_model()
router = Router(tags=["Users"])


@router.get("/me", response=UserReadSchema)
def get_me(request):
    return request.user


@router.patch("/me", response=UserReadSchema)
def update_me(request, data: UserUpdateSchema):
    user = request.user

    for field, value in data.dict(exclude_unset=True).items():
        setattr(user, field, value)

    user.save()
    return user
