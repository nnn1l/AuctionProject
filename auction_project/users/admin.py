from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'auction_wins', 'auction_hosted']

# Register your models here.
