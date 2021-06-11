from django.urls import reverse
from nose.tools import ok_, eq_
from rest_framework.test import APITestCase
from django.forms.models import model_to_dict
from rest_framework import status
from faker import Faker
import factory
from ..models import *
from .factories import  *
from ...users.test.factories import UserFactory

fake = Faker()

class TestProductListTestCase(APITestCase):
    """
    Tests /product list operations.
    """

    def setUp(self):
        self.url = reverse('product-list')

        #create product object, not saving product object
        product_build = ProductFactory.build()

        #save category and brand object
        product_build.category.save()
        product_build.brand.save()
        self.product_data = model_to_dict(product_build)

        """
        create and save new user object
        Include an appropriate `Authorization:` header on requests.
        """
        user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {user.auth_token}')


    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.product_data)
        # print('product-response: ', response.__dict__)
        eq_(response.status_code, status.HTTP_201_CREATED)
       
      
class TestProductDetailTestCase(APITestCase):
    """ 
    Tests /product detail operations.
    """

    def setUp(self):
        self.product = ProductFactory()
        self.url = reverse('product-detail', kwargs={'pk': self.product.pk})

        user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {user.auth_token}')

    def test_get_request_returns_a_given_product(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_patch_request_updates_a_product(self):
        
        new_title = fake.text()
        payload = {'title': new_title}
        response = self.client.patch(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)



class TestProductVariantListTestCase(APITestCase):
    """
    Tests /product-variant list operations.
    """

    def setUp(self):
        self.url = reverse('productvariant-list')
        productVariant_build = ProductVariantFactory.build()
        
        #create and save product object
        product = ProductFactory()
        productVariant_build.product = product
        
        self.data = model_to_dict(productVariant_build)

        user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {user.auth_token}')


    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.data)
        #print('product-response: ', response.__dict__)
        eq_(response.status_code, status.HTTP_201_CREATED)
       
      
class TestProductVariantDetailTestCase(APITestCase):
    """ 
    Tests /product-variant detail operations.
    """

    def setUp(self):
        self.productVariant = ProductVariantFactory()
        self.url = reverse('productvariant-detail', kwargs={'pk': self.productVariant.pk})

        user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {user.auth_token}')

    def test_get_request_returns_a_given_product_variant(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_patch_request_updates_a_product_variant(self):
        
        new_product = ProductFactory()
        payload = {'product': new_product.id}
        response = self.client.patch(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)


class TestProductVariantImagesListTestCase(APITestCase):
    """
    Tests /product-variant list operations.
    """

    def setUp(self):
        self.url = reverse('productvariantimages-list')
        productVariantImages_build = ProductVariantImagesFactory.build()
        productVariant = ProductVariantFactory()
        productVariantImages_build.product_varient = productVariant
        self.data = model_to_dict(productVariantImages_build)

        user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {user.auth_token}')


    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.data)
        eq_(response.status_code, status.HTTP_201_CREATED)
       

class TestProductVariantImagesDetailTestCase(APITestCase):
    """ 
    Tests /product-variant detail operations.
    """

    def setUp(self):
        self.productVariantImages = ProductVariantImagesFactory()
        self.url = reverse('productvariantimages-detail', kwargs={'pk': self.productVariantImages.pk})

        user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {user.auth_token}')

    def test_get_request_returns_a_given_product_variant_images(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_patch_request_updates_a_product_variant_images(self):
        
        new_productVariant = ProductVariantFactory()
        payload = {'product_varient': new_productVariant.id}
        response = self.client.patch(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)
