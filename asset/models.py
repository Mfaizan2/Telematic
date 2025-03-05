from django.db import models
from web.models import Web

class Asset(models.Model):
    name = models.CharField(max_length=50)
    phone_num = models.IntegerField()
    address = models.CharField(max_length=250)
    web = models.ForeignKey(Web, on_delete=models.CASCADE)

# Create your models here.
