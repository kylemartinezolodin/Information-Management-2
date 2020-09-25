from django.db import models
from datetime import datetime

# Create your models here.
# REQUIRED
class Customer(models.Model):
    customerId = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length = 25)
    middlename = models.CharField(max_length = 25, blank = True, null = True)
    lastname = models.CharField(max_length = 25)
    gender = models.BooleanField(blank = True, null = True)

    CUSTOMER_STATUS_CHOICES = [
        ('SD','Student'),
        ('SG','Single'),
        ('MR','Married')
    ]

    status = models.CharField(max_length=2, choices=CUSTOMER_STATUS_CHOICES, default='SG')

    birthday = models.DateField(blank = True, null = True)
    contactNumber = models.CharField(max_length = 11)
    email = models.EmailField(blank = True, null = True)
    class Meta:
        db_table = "Customer"
        
# REQUIRED
class Item(models.Model):
    itemId = models.AutoField(primary_key=True)

    ITEM_TYPE_CHOICES = [
        ('CPU','CPU'),
        ('GPU','GPU'),
        ('RAM','RAM'),
        ('SSD','SSD'),
        ('HDD','HDD'),
        ('NVM','NVMe'),
        ('PSU','PSU'),
        ('AVR','AVR'),
        ('MON','Monitor'),
        ('PRI','Printer'),
        ('KYB','Keyboard'),
        ('MSE','Mouse'),
    ]

    itemType = models.CharField(db_column = 'itemType', max_length=3, choices=ITEM_TYPE_CHOICES)
    brand = models.CharField(max_length = 25)
    itemName = models.CharField(max_length = 25)
    price = models.DecimalField(max_digits = 6, decimal_places=2)
    class Meta:
        db_table = "Item"

# OPTIONAL PWEDE RA IDELETE
class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    customerId = models.ForeignKey(db_column = 'customerId', to = 'dashboard.Customer', on_delete = models.SET_NULL, null = True)
    amount = models.DecimalField(max_digits = 6, decimal_places=2)
    orderDateTime = models.DateTimeField(auto_now = True)
    class Meta:
        db_table = "Order"

# OPTIONAL PWEDE RA IDELETE
class Cart(models.Model):
    cartId = models.AutoField(primary_key=True)
    orderId = models.OneToOneField(db_column = 'orderId', to = 'dashboard.Order', on_delete = models.SET_NULL, null = True)
    itemId = models.ForeignKey(db_column = 'itemId', to = 'dashboard.Item', on_delete = models.SET_NULL, null = True)
    quantity = models.DecimalField(max_digits = 6, decimal_places=0)
    class Meta:
        db_table = "Cart"
