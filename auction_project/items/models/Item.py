from django.db import models
from .Category import Category

class Item(models.Model):
    title = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item-images/')
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title