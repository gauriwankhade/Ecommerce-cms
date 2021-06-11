from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *

# Create your views here.
  

class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset  provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Order.
    """

    queryset= Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )


class OrderItemViewSet(viewsets.ModelViewSet):
    
    queryset= OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAuthenticated, )



   

