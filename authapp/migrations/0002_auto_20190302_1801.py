# Generated by Django 2.1.5 on 2019-03-02 15:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 4, 15, 1, 56, 157756, tzinfo=utc)),
        ),
    ]
