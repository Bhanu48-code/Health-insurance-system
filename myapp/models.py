from django.db import models
from django.db import models

# below code belongs to customer db table 
class MyApp(models.Model):
    
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'myappusers'  # this must match the MySQL table name
        managed = False


# below code belongs to employee db table 
class Myemployee(models.Model):
    
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'employee'  # must match the MySQL table name exactly
        managed = False        # prevents Django from modifying table

# below code belongs to employee admin users db table 
class MyadminUsers(models.Model):
    
    
    email = models.CharField(max_length=128)
    AdminPassword = models.CharField(max_length=128)

    class Meta:
        db_table = 'adminUsers'  # must match the MySQL table name exactly
        managed = False        # prevents Django from modifying table


#below code belongs to customers db table

class Customers(models.Model):
    
    
    NAME = models.CharField(max_length=128)
    GENDER = models.CharField(max_length=128)
    AADHAR_NO = models.CharField(max_length=128)
    PHONE_NUMBER = models.CharField(max_length=128)
    user_name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'customers'  # must match the MySQL table name exactly
        managed = False        # prevents Django from modifying table

# Create your models here.

