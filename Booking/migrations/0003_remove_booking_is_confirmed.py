# Generated by Django 4.2.6 on 2023-11-07 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0002_remove_booking_is_returned_booking_return_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='is_confirmed',
        ),
    ]
