# Generated by Django 3.1.4 on 2020-12-19 23:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20201219_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 20, 0, 48, 25, 338189)),
        ),
    ]
