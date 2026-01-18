from decimal import Decimal
from django.test import TestCase
from auctions.models.Auction import Auction
from auctions.models.Bid import Bid
from users.models.Wallet import Wallet
from users.tests.factories import UserFactory
from items.factories import ItemFactory
from auctions.tests.factories import AuctionFactory

class BidModelTest(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.other_user = UserFactory()

        self.wallet = Wallet.objects.get(user=self.user)
        self.other_wallet = Wallet.objects.get(user=self.other_user)

        self.auction = AuctionFactory(owner=self.other_user, start_price=Decimal('1000.00'))
        self.auction.current_price = self.auction.start_price
        self.auction.save()

    def test_bid_creation_updates_auction_and_wallet(self):
        """  Checking of creating bid: balance decreases, auction`s current price changes  """
        bid_amount = Decimal('1200.00')
        bid = Bid.objects.create(auction=self.auction, bidder=self.user, amount=bid_amount)

        # Checking auction`s current price
        self.auction.refresh_from_db()
        self.assertEqual(self.auction.current_price, bid_amount)

        # Checking balance decreasing
        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, Decimal('8800.00'))  # 10000 - 1200

        # Checking for bid`s saving
        self.assertEqual(Bid.objects.count(), 1)
        self.assertEqual(Bid.objects.first(), bid)

    def test_bid_too_low_raises_error(self):
        """  Bid is <= current price of auction  """
        Bid.objects.create(auction=self.auction, bidder=self.user, amount=Decimal('1200.00'))
        with self.assertRaises(ValueError):
            Bid.objects.create(auction=self.auction, bidder=self.user, amount=Decimal('1100.00'))

    def test_bid_with_insufficient_balance_raises_error(self):
        """  Bid is bigger than balance of bidder`s wallet  """
        self.wallet.balance = Decimal('500.00')
        self.wallet.save()

        with self.assertRaises(ValueError):
            Bid.objects.create(auction=self.auction, bidder=self.user, amount=Decimal('1000.00'))

    def test_bid_deletion_refunds_wallet(self):
        """  Money come back to bidder when bid is deleted  """
        bid_amount = Decimal('1200.00')
        bid = Bid.objects.create(auction=self.auction, bidder=self.user, amount=bid_amount)

        bid.delete()    # Delete a bid

        # Balance must come back
        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, Decimal('10000.00'))

