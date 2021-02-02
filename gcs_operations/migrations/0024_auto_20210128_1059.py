# Generated by Django 3.1.5 on 2021-01-28 10:59

from django.db import migrations, models
import gcs_operations.models


class Migration(migrations.Migration):

    dependencies = [
        ('gcs_operations', '0023_auto_20210128_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightoperation',
            name='name',
            field=models.CharField(default=gcs_operations.models.make_random_plan_common_name, max_length=30),
        ),
        migrations.AlterField(
            model_name='flightplan',
            name='name',
            field=models.CharField(default=gcs_operations.models.make_random_plan_common_name, max_length=30),
        ),
    ]