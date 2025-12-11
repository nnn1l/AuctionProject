from django.urls import path
from .views.items import ItemCreateView, ItemDetailView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path('create/', ItemCreateView.as_view(), name='item-create'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='item-details'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='item-update'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='item-delete')
    ]