from tkinter.font import names

from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import hello
from .views.settings_profile import UserRegisterView, UserLoginView, UserProfileView, UserUpdateProfileView, UsersItemsListView, UsersAuctionListView

urlpatterns = [
    path('all_users/', hello.users_list, name='user-list'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
    path('profile/<int:pk>/edit/', UserUpdateProfileView.as_view(), name='user-edit'),
    path('profile/<int:pk>/items/', UsersItemsListView.as_view(), name='user-items'),
    path('profile/<int:pk>/auctions/', UsersAuctionListView.as_view(), name='user-auctions'),
    ]