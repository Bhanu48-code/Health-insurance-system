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
class MyApp(models.Model):
    
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=128)

    class Meta:
        db_table = 'employee'  # this must match the MySQL table name
        managed = False


# Create your models here.

