from django.urls import path, include

from .views import hello

urlpatterns = [
    path('hello/', hello.hello, name = 'hello-users'),
    path('all_users/', hello.users_list, name='user-list'),
    path('register/', ..., name='user-register'),
    path('login/', ..., name='user-login'),
    path('logout/', ..., name='user-logout'),
    ]