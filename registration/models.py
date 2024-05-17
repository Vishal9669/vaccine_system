from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class registrat(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField( max_length=50)

    class Meta:
        db_table = 'registration_details'

class child(models.Model):
    parent = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    dob = models.DateField(auto_created=True)
    weight = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = 'child_details'