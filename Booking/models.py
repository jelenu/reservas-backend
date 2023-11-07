from django.db import models
from django.contrib.auth.models import User
from Vehicles.models import VehicleModel, Vehicle, Office

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)
    is_returned = models.BooleanField(default=False)
    assigned_vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    pickup_office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True, blank=True, related_name='pickup_reservations')
    return_office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True, blank=True, related_name='return_reservations')

    @property
    def is_assigned(self):
        return self.assigned_vehicle is not None

    def __str__(self):
        return f'{self.user.username} - {self.vehicle_model.model} - {self.start_date}'