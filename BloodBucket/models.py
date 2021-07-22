from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=70,primary_key= True)
    password = models.CharField(max_length=200)
    firstName = models.CharField(max_length=70)
    lastName = models.CharField(max_length=70)
