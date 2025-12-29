from django.db import models
from decimal import Decimal
from django.utils.translation import gettext_lazy as _

from .CustomUser import CustomUser

class Wallet(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='wallet',
        verbose_name=_('Owner')
    )

    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=10000,
        verbose_name=_('Balance')
    )

    def __str__(self):
        return f"{self.user.username}'s Wallet: {self.balance}"

    def can_afford(self, amount):
        """  Returns True or False in case if user is able to afford to place a bid or not  """
        return self.balance >= Decimal(amount)

#    def add_funds(self, amount):
#        self.balance += Decimal(amount)
#        self.save()

#    def deduct_funds(self, amount):
#        if self.can_afford(amount):
#            self.balance -= Decimal(amount)
#            self.save()
#            return True
#        return False

