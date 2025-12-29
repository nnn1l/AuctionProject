from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        verbose_name=_('Title')     #  <-- '_' is gettext_lazy()
    )

    description = models.CharField(
        max_length=300,
        null=True,
        verbose_name=_('Description')
    )

    def __str__(self):
        return self.title