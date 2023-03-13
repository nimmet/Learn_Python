from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    mobile = models.ImageField()
    
    def __str__(self):
        self.name = name 
        self.age = age
        self.mobile = mobile
        
        
    