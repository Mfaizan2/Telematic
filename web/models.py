from django.db import models
from customer.models import Customer

class Web(models.Model):
    name = models.CharField(max_length=50)
    phone_num = models.IntegerField()
    address = models.CharField(max_length=250)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

