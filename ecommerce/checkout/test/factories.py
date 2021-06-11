import factory, factory.fuzzy
from ...users.test.factories import UserFactory
from ...inventory.test.factories import ProductFactory


class OrderFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = "checkout.Order"
        django_get_or_create = ('id', )

    id = factory.Faker('uuid4')
    customer = factory.SubFactory(UserFactory)
    date_created = factory.Faker('date_time')
    status = False


class OrderItemFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = "checkout.OrderItem"
        django_get_or_create = ('id', )

    id = factory.Faker('uuid4')
    product = factory.SubFactory(ProductFactory)
    order = factory.SubFactory(OrderFactory)
    quantity = factory.fuzzy.FuzzyInteger(1, 10)

    
    
