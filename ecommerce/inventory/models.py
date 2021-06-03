from django.db import models
import uuid

# Create your models here.

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand_name = models.CharField(max_length=255)

    def __str__(self):
        return self.brand_name
  

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.title
  
class ProductVariant(models.Model):
    SIZE_CHOICES = [("XS","XS"), ("S","S"), ("M","M"), ("L","L"), ("XL","XL"), ("XXL","XXL"), ("XXXL","XXXL"), ("XXXXL","XXXXL")]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default= None)
    color = models.CharField(max_length=30, default=None)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.title + " size: " + self.size + " color: " + self.color

class ProductVariantImages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    product_varient = models.ForeignKey(ProductVariant,on_delete=models.CASCADE)
    image = models.FileField(upload_to='products')

    def __str__(self):
        return "Image for Product Varient: " + str(self.product_varient.id)









