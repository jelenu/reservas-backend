from django.db import models
from django.contrib.auth.models import User
from Vehicles.models import VehicleModel, Vehicle, Office

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    pickup_office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True, blank=True, related_name='pickup_reservations')

    def __str__(self):
        return f'{self.user.username} - {self.assigned_vehicle.model}'