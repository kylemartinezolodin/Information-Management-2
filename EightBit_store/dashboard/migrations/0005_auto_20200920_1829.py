# Generated by Django 3.1.1 on 2020-09-20 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200920_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2020, 9, 20, 18, 29, 12, 529805)),
        ),
    ]