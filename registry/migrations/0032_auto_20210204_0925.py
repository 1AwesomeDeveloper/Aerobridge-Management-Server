# Generated by Django 3.1.6 on 2021-02-04 09:25

from django.db import migrations, models
import registry.models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0031_auto_20210204_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorization',
            name='end_date',
            field=models.DateField(default=registry.models.two_year_expiration),
        ),
        migrations.AlterField(
            model_name='operator',
            name='expiration',
            field=models.DateField(default=registry.models.two_year_expiration),
        ),
    ]
