# Generated by Django 3.1.1 on 2020-09-20 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20200920_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Birthday',
            new_name='birthday',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='ContactNumber',
            new_name='contactNumber',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='CustomerId',
            new_name='customerId',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Firstname',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Lastname',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Middlename',
            new_name='middlename',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='Type',
            new_name='_type',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='Brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='ItemId',
            new_name='itemId',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='ItemName',
            new_name='itemName',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='Price',
            new_name='price',
        ),
        migrations.AlterModelTable(
            name='item',
            table='Item',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('orderDateTime', models.DateTimeField(auto_now_add=True)),
                ('customerId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.customer')),
            ],
            options={
                'db_table': 'Order',
            },
        ),
    ]