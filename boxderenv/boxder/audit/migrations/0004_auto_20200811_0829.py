# Generated by Django 3.0.5 on 2020-08-11 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0003_auto_20200810_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmodification',
            name='modification_time',
            field=models.TimeField(default=datetime.time(8, 29, 37, 224117)),
        ),
        migrations.AlterField(
            model_name='incomesandexits',
            name='departura_hour',
            field=models.TimeField(default=datetime.time(8, 29, 37, 222264)),
        ),
        migrations.AlterField(
            model_name='incomesandexits',
            name='hour_admission',
            field=models.TimeField(default=datetime.time(8, 29, 37, 222208)),
        ),
        migrations.AlterField(
            model_name='unauthorizedincome',
            name='try_hour',
            field=models.TimeField(default=datetime.time(8, 29, 37, 223221)),
        ),
        migrations.AlterField(
            model_name='usermodification',
            name='modification_time',
            field=models.TimeField(default=datetime.time(8, 29, 37, 221173)),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='creation_time',
            field=models.TimeField(default=datetime.time(8, 29, 37, 220178)),
        ),
    ]