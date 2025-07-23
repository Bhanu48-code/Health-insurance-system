from django.db import models
from django.db import models

class MyApp(models.Model):
    
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'myappusers'  # this must match the MySQL table name
        managed = False

# Create your models here.
