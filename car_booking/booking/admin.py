from django.contrib import admin
from .models import Vehicle, Booking, Result


# Register your models here.

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'vehicle_type', 'location', 'date', 'time', 'price')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'total_price', 'booking_time', 'payment_method')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('booking', 'status', 'rating', 'feedback')

