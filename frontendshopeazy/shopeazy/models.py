from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length=255, primary_key = True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    type = models.CharField(max_length=2, default ='C')
    
