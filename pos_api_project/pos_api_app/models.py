from django.db import models

# Create your models here.
from django.db import models
    
class Category(models.Model):
    name = models.CharField(max_length=150)
    colorCode = models.CharField(max_length=10),
    createTime = models.DateTimeField()
    updateTime = models.DateTimeField()

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        primary_key=True,
        db_constraint=False
    )
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    price = models.FloatField()
    thumbUrl = models.CharField(max_length=15)
    createTime = models.DateTimeField()
    updateTime = models.DateTimeField()