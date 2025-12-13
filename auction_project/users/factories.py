import factory
from .models.CustomUser import CustomUser
from django.contrib.auth.hashers import make_password

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser


    username = factory.Sequence(lambda n: f'testuser-{n}')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@gmail.com')
    password = make_password('password')
    biography = factory.Faker('Hi! This is my bio.')
