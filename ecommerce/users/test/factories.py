import factory


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'users.User'
        django_get_or_create = ('username',)

    id = factory.Faker('uuid4')
    # username = factory.Sequence(lambda n: f'testuser{n}')
    username = factory.Faker('email')
    password = factory.Faker('password', length=10, special_chars=True, digits=True,
                             upper_case=True, lower_case=True)
                             
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    #is_staff = False
    is_superuser = True


class AddressFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'users.Address'
        django_get_or_create = ('id',)

    id = factory.Faker('uuid4')
    customer = factory.SubFactory(UserFactory)
    line1 = factory.Faker('building_number')
    line2 = factory.Faker('street_address')
    city = factory.Faker('city')
    state = "Navada"
    country = factory.Faker('country')
    zipcode = factory.Faker('postcode')