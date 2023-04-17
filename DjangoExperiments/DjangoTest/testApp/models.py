from django.db import models

# Create your models here.

class Net(models.Model):
    name = models.CharField(max_length=20)
    size = models.IntegerField()
    
    
class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()