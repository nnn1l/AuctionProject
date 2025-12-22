from django.db import models
from decimal import Decimal

from .CustomUser import CustomUser

class Wallet(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=10000)

    def __str__(self):
        return f"{self.user.username}'s Wallet: {self.balance}"

    def can_afford(self, amount):
        return self.balance >= Decimal(amount)

    def add_funds(self, amount):
        self.balance += Decimal(amount)
        self.save()

    def deduct_funds(self, amount):
        if self.can_afford(amount):
            self.balance -= Decimal(amount)
            self.save()
            return True
        return False

