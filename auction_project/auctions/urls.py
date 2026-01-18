from django.urls import path
from .views.auctions import AuctionCreateView, AuctionDeleteView, AuctionDetailView, AuctionUpdateView, AuctionEndView
from .views.bids import BidCreateView
from .views.all_auctions import auction_list

urlpatterns = [
    path('create/', AuctionCreateView.as_view(), name='auction-create'),
    path('update/<int:pk>/', AuctionUpdateView.as_view(), name='auction-update'),
    path('details/<int:pk>/', AuctionDetailView.as_view(), name='auction-details'),
    path('delete/<int:pk>/', AuctionDeleteView.as_view(), name='auction-delete'),
    path('all_auctions/', auction_list, name='auction-list'),
    path('create/<int:pk>/bid/', BidCreateView.as_view(), name='bid-create'),
    path('auction/<int:pk>/end/', AuctionEndView.as_view(), name='auction-end')
    ]