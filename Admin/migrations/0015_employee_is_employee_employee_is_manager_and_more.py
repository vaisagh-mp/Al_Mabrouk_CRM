# Generated by Django 5.1.4 on 2025-01-16 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0014_attendance_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_employee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='rank',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]