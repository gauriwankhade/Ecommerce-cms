from django.db import models
from ecommerce.users.models import User
from ecommerce.inventory.models import Product
import uuid

# Create your models here.

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return "Order by: " + self.customer.username 


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


    def __str__(self):
        return "Order Item of: " + str(self.order.id)


