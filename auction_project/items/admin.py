from django.contrib import admin
from .models import Item, Category

@admin.register(Item, Category)
class AdminItemCategory(admin.ModelAdmin):
    pass

# Register your models here.
