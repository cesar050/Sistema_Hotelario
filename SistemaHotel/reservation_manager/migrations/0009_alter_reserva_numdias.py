# Generated by Django 5.0.6 on 2024-06-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_manager', '0008_remove_reserva_servicios_reserva_total_costo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='numDias',
            field=models.IntegerField(default=0),
        ),
    ]
