import factory
from .models.Item import Item, Category
from users.factories import UserFactory

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Sequence(lambda n: f"Category {n}")
    description = factory.LazyAttribute(lambda obj: f'{obj.title}')



class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    title = factory.Sequence(lambda n: f'test-item{n}')
    category = factory.SubFactory(CategoryFactory)
    description = factory.Faker('sentence', nb_words=6)
    owner = factory.SubFactory(UserFactory)
