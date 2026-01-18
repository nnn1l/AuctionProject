from decimal import Decimal

import factory
from users.models.CustomUser import CustomUser
from users.models.Wallet import Wallet
from django.contrib.auth.hashers import make_password

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser


    username = factory.Sequence(lambda n: f'testuser-{n}')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@gmail.com')
    password = make_password('password')
    biography = factory.Faker('sentence', nb_words=6)


class WalletFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Wallet

    user = factory.SubFactory(UserFactory)
    balance = Decimal('10000.00')