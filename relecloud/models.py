from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,)
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False,)
    

class Cruise(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,)
    duration = models.IntegerField(
        null=False,
        blank=False,)
    price = models.FloatField(
        null=False,
        blank=False,)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

class InfoRequest(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,)
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False,)
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE)