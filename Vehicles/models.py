from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

class Office(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class VehicleModel(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year_of_manufacture = models.PositiveIntegerField()
    seats = models.PositiveSmallIntegerField()
    doors = models.PositiveSmallIntegerField()
    transmission = models.CharField(max_length=20, choices=(('Manual', 'Manual'), ('Automatic', 'Automatic')))
    image = models.ImageField(upload_to='vehicle_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.brand} {self.model} ({self.year_of_manufacture})'

@receiver(pre_delete, sender=VehicleModel)
def delete_vehicle_image(sender, instance, **kwargs):
    # Borra la imagen asociada al objeto cuando se elimina el vehículo
    if instance.image:
        # Asegúrate de eliminar la imagen físicamente del sistema de archivos
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

# Registra la señal para que sea conectada cuando se elimina un objeto VehicleModel
pre_delete.connect(delete_vehicle_image, sender=VehicleModel)


class Vehicle(models.Model):
    model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=10, unique=True)
    location = models.ForeignKey(Office, on_delete=models.CASCADE,  null=True, blank=True) 

    def __str__(self):
        return f'{self.model} - {self.license_plate}'
    

