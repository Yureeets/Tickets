from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class Flight(models.Model):
    origin_city = models.CharField(max_length=64)
    origin_code = models.CharField(max_length=3)
    origin_country = models.CharField(max_length=64)

    destination_city = models.CharField(max_length=64)
    destination_code = models.CharField(max_length=3)
    destination_country = models.CharField(max_length=64)

    depart_time = models.TimeField()
    duration = models.DurationField()
    plane = models.CharField(max_length=24)
    airline = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.origin_city}, {self.origin_country} ({self.origin_code}) to {self.destination_city}, {self.destination_country} ({self.destination_code})"


class Passenger(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}"


class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="tickets")
    passengers = models.ManyToManyField(Passenger, related_name="flight_tickets")
    seat_class = models.CharField(max_length=20)
    booking_date = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=45)
