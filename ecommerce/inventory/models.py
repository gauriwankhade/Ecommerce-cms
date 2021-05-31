from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    size = 
    

    def __str__():
        return self.title

    
class ProductVariant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)




