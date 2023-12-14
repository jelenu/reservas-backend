from django.db import models

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
    


class Vehicle(models.Model):
    model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=10, unique=True)
    location = models.ForeignKey(Office, on_delete=models.CASCADE,  null=True, blank=True) 

    def __str__(self):
        return f'{self.model} - {self.license_plate}'
    

