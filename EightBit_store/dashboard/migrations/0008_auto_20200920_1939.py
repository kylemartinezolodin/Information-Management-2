# Generated by Django 3.1.1 on 2020-09-20 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20200920_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('ItemId', models.AutoField(primary_key=True, serialize=False)),
                ('Type', models.CharField(choices=[('CPU', 'CPU'), ('GPU', 'GPU'), ('RAM', 'RAM'), ('SSD', 'SSD'), ('HDD', 'HDD'), ('NVM', 'NVMe'), ('PSU', 'PSU'), ('AVR', 'AVR'), ('MON', 'Monitor'), ('PRI', 'Printer'), ('KYB', 'Keyboard'), ('MSE', 'Mouse')], max_length=3)),
                ('Brand', models.CharField(max_length=25)),
                ('ItemName', models.CharField(max_length=25)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='birthday',
            new_name='Birthday',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='contactNumber',
            new_name='ContactNumber',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customerId',
            new_name='CustomerId',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='firstname',
            new_name='Firstname',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='gender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='lastname',
            new_name='Lastname',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='middlename',
            new_name='Middlename',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='status',
            new_name='Status',
        ),
    ]
