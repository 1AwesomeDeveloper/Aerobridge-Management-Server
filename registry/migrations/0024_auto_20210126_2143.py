# Generated by Django 3.1.5 on 2021-01-26 21:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0023_auto_20210123_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorization',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 26, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='operator',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 26, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registry.person'),
        ),
    ]
