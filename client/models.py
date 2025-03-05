from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=50)
    phone_num = models.IntegerField()
    address = models.CharField(max_length=250)