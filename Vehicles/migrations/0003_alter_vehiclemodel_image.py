# Generated by Django 4.2.6 on 2023-11-07 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicles', '0002_vehiclemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle_images/'),
        ),
    ]
