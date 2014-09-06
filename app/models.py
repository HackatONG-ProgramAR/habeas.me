from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    city_id = models.IntegerField()
    address = models.CharField(max_length = 300)
    ttl = models.DateTimeField()

