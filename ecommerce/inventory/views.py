from django.shortcuts import render
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from .serializers import *
from .models import *

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset  provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Product.
    """

    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )
   



class ProductVariantViewSet(viewsets.ModelViewSet):
    queryset= ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer
    permission_classes = (IsAdminOrReadOnly, )


class ProductVariantImagesViewSet(viewsets.ModelViewSet):
    queryset= ProductVariantImages.objects.all()
    serializer_class = ProductVariantImagesSerializer
    permission_classes = (IsAdminOrReadOnly, )
    


class BrandViewSet(viewsets.ModelViewSet):
    queryset= Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (IsAdminOrReadOnly, )
   

class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly, )
    








