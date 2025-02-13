from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50) 
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} ({self.location})"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="bookings")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_time = models.TimeField() 
    payment_method = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"

class Result(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name="result")
    
    STATUS_CHOICES = [
        ('failed', 'Failed'),
        ('success', 'Success'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    
    RATING_CHOICES = [
        (1, '1 - Very Bad'),
        (2, '2 - Bad'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    feedback = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Result for Booking {self.booking.id}: {self.status}"
