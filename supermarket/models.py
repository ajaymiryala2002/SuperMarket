from django.db import models

class order(models.Model):
    PRODUCT_NAME=models.CharField(max_length=20)
    Mobile_number=models.CharField(max_length=10)
    Quantities=models.IntegerField()
    




