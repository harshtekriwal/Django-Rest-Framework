from django.db import models
from django.db.models.lookups import StartsWith
from simple_history.models import HistoricalRecords
from rest_framework import serializers
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    # ID will be auto-generated


class Home(models.Model):
    ROOM_CHOICES = (
        ("1BHK", "1BHK"),
        ("2BHK", "2BHK"),
        ("3BHK", "3BHK")

    )
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    price = models.IntegerField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='HomeOwned')
    room_type = models.CharField(
        max_length=4, choices=ROOM_CHOICES, default="1BHK")


class BookingHistory(models.Model):
    booked_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='History')

    house_id = models.ForeignKey(
        Home, on_delete=models.CASCADE, related_name='History')

    start_date = models.DateField()
    end_date = models.DateField()
