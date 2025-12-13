from tkinter.font import names

from django.urls import path
from .views import AuctionCreateView, AuctionDeleteView, AuctionDetailView, AuctionUpdateView

urlpatterns = [
    path('create/', AuctionCreateView.as_view(), name='auction-create'),
    path('update/<int:pk>/', AuctionUpdateView.as_view(), name='auction-update'),
    path('details/<int:pk>/', AuctionDetailView.as_view(), name='auction-details'),
    path('delete/<int:pk>/', AuctionDeleteView.as_view(), name='auction-delete')
    ]