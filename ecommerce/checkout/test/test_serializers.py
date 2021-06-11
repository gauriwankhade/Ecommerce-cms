from django.test import TestCase
from django.forms.models import model_to_dict  
from nose.tools import eq_, ok_
from .factories import *
from ..serializers import *


class TestOrderSerializer(TestCase):

    def setUp(self):
        self.order_data = model_to_dict(OrderFactory())

    def test_serializer_with_empty_data(self):
        serializer = OrderSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = OrderSerializer(data=self.order_data)
        ok_(serializer.is_valid())


class TestOrderItemSerializer(TestCase):

    def setUp(self):
        self.orderitem_data = model_to_dict(OrderItemFactory())

    def test_serializer_with_empty_data(self):
        serializer = OrderItemSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = OrderItemSerializer(data=self.orderitem_data)
        ok_(serializer.is_valid())

