from ninja import Router
from django.contrib.auth import get_user_model
from users.pydantic import WalletOut

User = get_user_model()

router = Router(tags=["Wallets"])


@router.get("/me", response=WalletOut)
def get_my_wallet(request):
    wallet = request.user.wallet
    return wallet
