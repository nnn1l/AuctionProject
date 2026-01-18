import factory
from decimal import Decimal
from django.utils import timezone
from auctions.models.Auction import Auction
from users.tests.factories import UserFactory


class AuctionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Auction

    title = factory.Sequence(lambda n: f'Auction {n}')
    description = factory.Faker('sentence', nb_words=6)
    owner = factory.SubFactory(UserFactory)
    start_price = Decimal('1000.00')
    current_price = Decimal('1000.00')
    is_active = True
    end_time = factory.LazyFunction(
        lambda: timezone.now() + timezone.timedelta(days=7)
    )
