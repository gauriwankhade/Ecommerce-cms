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
from ...inventory.test.factories import ProductFactory


class TestOrderListTestCase(APITestCase):
    """
    Tests /order list operations.
    """

    def setUp(self):
        self.url = reverse('order-list')
        """
        create and save new user object
        Include an appropriate `Authorization:` header on requests.
        """
        user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {user.auth_token}')
        
        #create order object, not saving order object
        order_build = OrderFactory.build()

        #save customer object
        order_build.customer = user

        self.order_data = model_to_dict(order_build)


    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.order_data)
        eq_(response.status_code, status.HTTP_201_CREATED)



class TestOrderDetailTestCase(APITestCase):

    """ 
    Tests /order detail operations.
    """

    def setUp(self):
        self.order = OrderFactory()
        self.url = reverse('order-detail', kwargs={'pk': self.order.pk})

        user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {user.auth_token}')

    def test_get_request_returns_a_given_order(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_patch_request_updates_a_order(self):
        
        new_status = True
        payload = {'status': new_status}
        response = self.client.patch(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)



class TestOrderItemListTestCase(APITestCase):
    """
    Tests /orderitem list operations.
    """

    def setUp(self):
        self.url = reverse('orderitem-list')
        """
        create and save new user object
        Include an appropriate `Authorization:` header on requests.
        """
        user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {user.auth_token}')
        
        #create orderitem object, not saving orderitem object
        orderitem_build = OrderItemFactory.build()

        #create product and order object
        product = ProductFactory()
        order = OrderFactory()

        #update product and order for orderitem object
        orderitem_build.product = product
        orderitem_build.order = order

        self.orderitem_data = model_to_dict(orderitem_build)


    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.orderitem_data)
        eq_(response.status_code, status.HTTP_201_CREATED)


class TestOrderItemDetailTestCase(APITestCase):

    """ 
    Tests /orderitem detail operations.
    """

    def setUp(self):
        self.orderitem = OrderItemFactory()
        self.url = reverse('orderitem-detail', kwargs={'pk': self.orderitem.pk})

        user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {user.auth_token}')

    def test_get_request_returns_a_given_orderitem(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_patch_request_updates_a_order(self):
        
        new_product = ProductFactory()
        payload = {'product': new_product.id}
        response = self.client.patch(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)



