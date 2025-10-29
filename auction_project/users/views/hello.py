from django.shortcuts import render
from django.http import response
from ..models import CustomUser

# Create your views here.

def hello(request):
    return response.HttpResponse("Hello")

def users_list(request):
    template_name = 'all-users.html'
    all_users = CustomUser.objects.all()
    return render(request, "all-users.html", {"users": all_users})
