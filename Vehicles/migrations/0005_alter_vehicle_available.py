# Generated by Django 4.2.6 on 2023-11-25 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicles', '0004_alter_vehicle_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='available',
            field=models.DateField(blank=True, null=True),
        ),
    ]