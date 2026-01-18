from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from items.models.Item import Item
from auctions.models.Auction import Auction
from users.models.Wallet import Wallet
from users.tests.factories import UserFactory, WalletFactory
from items.factories import ItemFactory, CategoryFactory
from auctions.tests.factories import AuctionFactory
from auctions.models.Bid import Bid


class AuctionViewsTest(TestCase):

    def setUp(self):
        self.user = UserFactory(password='password')
        self.user.set_password('password')
        self.user.save()
        self.wallet = Wallet.objects.get(user=self.user)

        self.other_user = UserFactory()

        self.category = CategoryFactory()
        self.item = ItemFactory(owner=self.user, category=self.category)

        self.auction = AuctionFactory(owner=self.user)
        self.auction.attach_items(
            Item.objects.filter(pk=self.item.pk)
        )

        self.client.login(username=self.user.username, password='password')

    # CREATE
    def test_auction_create_view_post(self):
        url = reverse('auction-create')
        data = {
            'title': 'New Auction',
            'description': 'Test description',
            'start_price': '150.00',
            'end_time': '2099-12-31 23:59',
            'items': [self.item.pk],
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # redirect
        auction = Auction.objects.get(title='New Auction')
        self.assertEqual(auction.start_price, Decimal('150.00'))
        self.assertIn(self.item, auction.items.all())

    # DETAIL
    def test_auction_detail_view(self):
        url = reverse('auction-details', kwargs={'pk': self.auction.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.auction.title)
        self.assertContains(response, self.item.title)

    # UPDATE
    def test_auction_update_view_post(self):
        url = reverse('auction-update', kwargs={'pk': self.auction.pk})
        data = {
            'title': 'Updated Auction',
            'description': 'Updated desc',
            'start_price': '200.00',
            'end_time': '2099-12-31 23:59',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.auction.refresh_from_db()
        self.assertEqual(self.auction.title, 'Updated Auction')
        self.assertEqual(self.auction.start_price, Decimal('200.00'))

    # DELETE
    def test_auction_delete_view(self):
        url = reverse('auction-delete', kwargs={'pk': self.auction.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Auction.objects.filter(pk=self.auction.pk).exists())

    # END AUCTION
    def test_auction_end_view(self):
        url = reverse('auction-end', kwargs={'pk': self.auction.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.auction.refresh_from_db()
        self.assertFalse(self.auction.is_active)



