from django.contrib import admin
from .models import Auction

@admin.register(Auction)
class AdminAuction(admin.ModelAdmin):
    list_display = ['title', 'description', 'start_time', 'end_time', 'is_active', 'owner', 'start_price']


# Register your models here.
