# Generated by Django 5.1.4 on 2025-01-04 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_alter_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='travel_in_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='travel_out_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]