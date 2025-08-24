from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title