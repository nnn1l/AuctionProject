from django.contrib import admin
from .models import Item, Category

@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    list_display = ['title', 'category', 'image', 'description', 'owner', 'auction']

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['title', 'description']

# Register your models here.
