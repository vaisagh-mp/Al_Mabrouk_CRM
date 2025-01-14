# Generated by Django 5.1.4 on 2025-01-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_attendance_rejected_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('ONGOING', 'Ongoing'), ('HOLD', 'Hold'), ('CANCELLED', 'Cancelled'), ('COMPLETED', 'Completed')], default='PENDING', max_length=100),
        ),
    ]