from django.urls import path

from .views import hello

urlpatterns = [
    path('hello/', hello.hello, name = 'hello-users'),
    path('all_users/', hello.users_list, name='user-list'),
    ]