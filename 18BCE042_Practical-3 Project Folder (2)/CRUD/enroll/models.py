from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=20)
    mname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    mobno = models.CharField(max_length=15)
    alemail = models.EmailField(max_length=100)
    almobno = models.CharField(max_length=15)
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    insname = models.CharField(max_length=20)