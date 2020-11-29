# Generated by Django 3.1.3 on 2020-11-24 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcs_operations', '0002_auto_20201124_1135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drone',
            old_name='drone_type_id',
            new_name='type_id',
        ),
        migrations.AddField(
            model_name='drone',
            name='is_registered',
            field=models.BooleanField(default=False),
        ),
    ]