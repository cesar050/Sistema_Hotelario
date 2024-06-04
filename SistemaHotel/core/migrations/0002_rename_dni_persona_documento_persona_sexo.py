# Generated by Django 5.0.6 on 2024-06-01 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='dni',
            new_name='documento',
        ),
        migrations.AddField(
            model_name='persona',
            name='sexo',
            field=models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMENINO')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
