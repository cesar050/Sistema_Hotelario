# Generated by Django 5.0.6 on 2024-06-04 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_manager', '0005_remove_reserva_servicios'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='total_costo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
