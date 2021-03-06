# Generated by Django 3.1.6 on 2021-02-02 22:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0027_auto_20210128_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_line_3',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='postcode',
            field=models.CharField(max_length=10, verbose_name='post code'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 2, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='operator',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 2, 0, 0, tzinfo=utc)),
        ),
    ]
