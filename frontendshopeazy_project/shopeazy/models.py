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
    
class Product(models.Model):
    productid = models.IntegerField(primary_key = True)
    pname = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.CharField(max_length=255)
    specifications = models.CharField(max_length=255)
    image = models.CharField(max_length=255, default="")

# id is auto-generated and incremented by django
class Order(models.Model):
    userid = models.ForeignKey(User, on_delete = models.CASCADE)
    productid = models.ForeignKey(Product, on_delete = models.CASCADE)
    # quantity = models.IntegerField(default=1)
    orderdate = models.DateTimeField(auto_now_add = True)
    orderstatus = models.CharField(max_length=255)
    finalprice = models.FloatField()

# promo code is of 5 letters
#auto generated id == primary key
class Cart(models.Model):
    productlist = models.CharField(max_length=255)
    promocode = models.CharField(max_length=5)
    
    
    
