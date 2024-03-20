from django.db import models

# Create your models here.

class booking(models.Model):
    """Maps to the Booking Table"""
    id = models.AutoField(primary_key=True,default="1")
    name = models.CharField(max_length=150)
    no_of_guest = models.IntegerField()
    booking_date =models.IntegerField()

class menu(models.Model):
    ''' Model for Menu'''
    id = models.AutoField(primary_key=True,default="1")
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    inventory =models.IntegerField()


