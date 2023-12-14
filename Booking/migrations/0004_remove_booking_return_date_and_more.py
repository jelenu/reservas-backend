# Generated by Django 4.2.6 on 2023-12-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0003_remove_booking_is_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='return_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='return_office',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='vehicle_model',
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateField(),
        ),
    ]