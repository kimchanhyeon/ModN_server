from django.db import models

# Create your models here.


class OrderPayment(models.Model):
    method = models.CharField(max_length="")