# Generated by Django 3.1.4 on 2020-12-21 22:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20201221_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 21, 23, 58, 21, 984757)),
        ),
    ]
