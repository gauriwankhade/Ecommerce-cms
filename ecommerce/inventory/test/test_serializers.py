from django.test import TestCase
from django.forms.models import model_to_dict
from nose.tools import eq_, ok_
from .factories import *
from ..serializers import *


class TestCategorySerializer(TestCase):

    def setUp(self):
        self.category_data = model_to_dict(CategoryFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = CategorySerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = CategorySerializer(data=self.category_data)
        ok_(serializer.is_valid())


class TestBrandSerializer(TestCase):

    def setUp(self):
        self.brand_data = model_to_dict(BrandFactory.build())
    
    def test_serializer_with_empty_data(self):
        serializer = BrandSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = BrandSerializer(data=self.brand_data)
        ok_(serializer.is_valid())



class TestProductSerializer(TestCase):

    def setUp(self):
        self.product_data = model_to_dict(ProductFactory())
       
    def test_serializer_with_empty_data(self):
        serializer = ProductSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = ProductSerializer(data=self.product_data)
        #ok_(serializer.is_valid(raise_exception=True))
        ok_(serializer.is_valid())
        

    
class TestProductVariantSerializer(TestCase):

    def setUp(self):
        self.data = model_to_dict(ProductVariantFactory())
       
    def test_serializer_with_empty_data(self):
        serializer = ProductVariantSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = ProductVariantSerializer(data=self.data)
        #ok_(serializer.is_valid(raise_exception=True))
        ok_(serializer.is_valid())
        

class TestProductVariantImagesSerializer(TestCase):

    def setUp(self):
        self.data = model_to_dict(ProductVariantImagesFactory())
       
    def test_serializer_with_empty_data(self):
        serializer = ProductVariantSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = ProductVariantImagesSerializer(data=self.data)
        #ok_(serializer.is_valid(raise_exception=True))
        ok_(serializer.is_valid())
        

    