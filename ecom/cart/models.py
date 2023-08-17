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