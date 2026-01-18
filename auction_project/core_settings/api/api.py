from ninja import NinjaAPI
from .wallets import router as wallets_router
from .items import router as items_router
from .auctions import router as auctions_router
from .bids import router as bids_router
from .users import router as users_router

api = NinjaAPI(
    title="Auction API",
    version="1.0"
)

api.add_router("wallets", wallets_router)
api.add_router("items", items_router)
api.add_router("auctions", auctions_router)
api.add_router("bids", bids_router)
api.add_router("users", users_router)
