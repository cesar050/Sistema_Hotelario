# Generated by Django 5.0.6 on 2024-06-04 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='numDias',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]