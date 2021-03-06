# Generated by Django 3.1.1 on 2020-09-24 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20200921_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='_type',
            field=models.CharField(choices=[('CPU', 'CPU'), ('GPU', 'GPU'), ('RAM', 'RAM'), ('SSD', 'SSD'), ('HDD', 'HDD'), ('NVM', 'NVMe'), ('PSU', 'PSU'), ('AVR', 'AVR'), ('MON', 'Monitor'), ('PRI', 'Printer'), ('KYB', 'Keyboard'), ('MSE', 'Mouse')], db_column='type', max_length=3),
        ),
    ]
