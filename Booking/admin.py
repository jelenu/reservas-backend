from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle_model', 'start_date', 'end_date', 'is_confirmed', 'is_assigned', 'pickup_office', 'return_office')
    
    def is_assigned(self, obj):
        return obj.is_assigned
    is_assigned.boolean = True
