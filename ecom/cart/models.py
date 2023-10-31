from django.db import models
from django . contrib . auth . models import User
from ecomapp.models import Products

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.user,self.product)
    
    class Meta:
        ordering = ['-created']

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return '{}-{}'.format(self.user,self.product)
    
    class Meta:
        ordering = ['-created']

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('packed','packed'),
    ('on the way','on the way'),
    ('Delivered','Delivered'),
    ('cancel','cancel'),
    ('pending','pending'),

)

class Orders(models.Model):
    First_name = models.CharField(max_length=200)
    Second_name = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.IntegerField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField(null=True,blank=True)
    district = models.CharField(max_length=200,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='pending' , null=True,blank=True)

    def __str__(self):
        return '{}-{}'.format(self.First_name,self.Second_name)

class Profile(models.Model):
    First_name = models.CharField(max_length=200)
    Second_name = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.IntegerField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField(null=True,blank=True)
    district = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return '{}-{}'.format(self.First_name,self.Second_name)


class OrderItems(models.Model):
    orders = models.ForeignKey(Orders,on_delete=models.CASCADE)
    products = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.orders}"