# Generated by Django 5.1.7 on 2025-04-03 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0002_parkingarea_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parkingslot',
            old_name='area',
            new_name='parking_area',
        ),
        migrations.RemoveField(
            model_name='parkingslot',
            name='status',
        ),
        migrations.AddField(
            model_name='parkingslot',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='parkingslot',
            name='slot_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
