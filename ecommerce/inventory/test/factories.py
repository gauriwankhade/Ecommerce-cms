import factory
import factory.fuzzy
 

class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'inventory.Category'
        django_get_or_create = ('id',)

    id = factory.Faker('uuid4')
    category_name = factory.Faker('sentence', nb_words=1)
    
class BrandFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'inventory.Brand'
        django_get_or_create = ('id',)
        
    id = factory.Faker('uuid4')
    brand_name = factory.Faker('sentence', nb_words=1)


class ProductFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'inventory.Product'
        django_get_or_create = ('id',)

    id = factory.Faker('uuid4')
    title = factory.Faker('sentence', nb_words=2)
    description = factory.Faker('sentence', nb_words=5)
    category = factory.SubFactory(CategoryFactory)
    brand = factory.SubFactory(BrandFactory)



class ProductVariantFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'inventory.ProductVariant'
        django_get_or_create = ('id',)

    id = factory.Faker('uuid4')
    product = factory.SubFactory(ProductFactory)
    size = "XL"
    color = "Blue"
    price = factory.fuzzy.FuzzyInteger(1, 9999)


class ProductVariantImagesFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'inventory.ProductVariantImages'
        django_get_or_create = ('id',)

    id = factory.Faker('uuid4')
    product_varient = factory.SubFactory(ProductVariantFactory)
    image = "products/bag.jpg"
    
