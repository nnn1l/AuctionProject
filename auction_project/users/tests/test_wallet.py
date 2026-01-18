from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model

from users.models.Wallet import Wallet
from users.tests.factories import UserFactory

User = get_user_model()


class WalletModelTest(TestCase):

    def test_wallet_created_by_signal(self):
        user = UserFactory()

        self.assertTrue(
            Wallet.objects.filter(user=user).exists()
        )

    def test_wallet_default_balance(self):
        user = UserFactory()
        wallet = user.wallet

        self.assertEqual(wallet.balance, Decimal('10000.00'))

    def test_can_afford_true(self):
        user = UserFactory()
        wallet = user.wallet
        wallet.balance = Decimal('5000')
        wallet.save()

        self.assertTrue(wallet.can_afford(Decimal('1000')))

    def test_can_afford_false(self):
        user = UserFactory()
        wallet = user.wallet
        wallet.balance = Decimal('500')
        wallet.save()

        self.assertFalse(wallet.can_afford(Decimal('1000')))

    def test_balance_decrease(self):
        user = UserFactory()
        wallet = user.wallet
        wallet.balance = Decimal('2000')
        wallet.save()

        wallet.balance -= Decimal('750')
        wallet.save()

        wallet.refresh_from_db()
        self.assertEqual(wallet.balance, Decimal('1250.00'))