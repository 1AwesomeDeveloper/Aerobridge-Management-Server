# Generated by Django 3.1.3 on 2020-11-30 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0019_auto_20201130_1207'),
        ('gcs_operations', '0008_auto_20201130_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightoperation',
            name='purpose',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registry.activity'),
        ),
        migrations.AlterField(
            model_name='flightoperation',
            name='name',
            field=models.CharField(default='Flight Operation wmsdcn', max_length=20),
        ),
        migrations.AlterField(
            model_name='flightplan',
            name='name',
            field=models.CharField(default='Flight Plan pxquda', max_length=20),
        ),
    ]
