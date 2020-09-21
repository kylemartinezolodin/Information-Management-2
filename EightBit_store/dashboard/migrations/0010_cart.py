# Generated by Django 3.1.1 on 2020-09-20 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20200921_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cartId', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=6)),
                ('itemId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.item')),
                ('orderId', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.order')),
            ],
            options={
                'db_table': 'Cart',
            },
        ),
    ]
