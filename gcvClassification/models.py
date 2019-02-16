from django.db import models

# Create your models here.
class Category(models.Model):
    description = models.CharField(max_length=250, null=False)

class Product(models.Model):
    category = models.CharField(max_length=250, null=False) #.ForeignKey(Categories, on_delete=models.CASCADE)
    percentage = models.FloatField(null=False)
    image_path = models.CharField(max_length=250, null=False)