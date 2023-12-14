from django.contrib import admin
from .models import VehicleModel, Vehicle, Office

@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year_of_manufacture', 'seats', 'doors', 'transmission')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('model', 'license_plate', 'location')

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')