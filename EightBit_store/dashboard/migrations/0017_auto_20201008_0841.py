# Generated by Django 3.1.1 on 2020-10-08 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20201005_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='orderId',
            field=models.ForeignKey(db_column='orderId', null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.order'),
        ),
    ]