# Generated by Django 4.2.6 on 2023-11-25 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicles', '0003_alter_vehiclemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='available',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
