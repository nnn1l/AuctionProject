from django.contrib import admin
from .models import Auction

@admin.register(Auction)
class AdminAuction(admin.ModelAdmin):
    list_display = ['item', 'start_time', 'end_time']

# Register your models here.
