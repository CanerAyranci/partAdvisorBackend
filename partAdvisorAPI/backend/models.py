from django.db import models

class Tire(models.Model):

    id = models.IntegerField(primary_key=True)
    model_id = models.IntegerField()
    brand = models.CharField(max_length = 200)
    model = models.CharField(max_length = 400)
    tireSpecs = models.CharField(max_length= 10)
    mevsim = models.CharField(max_length= 100)
    fuelNote = models.CharField(max_length= 1)
    performance = models.CharField(max_length= 25)
    price = models.IntegerField()

    def __str__(self):
        return self.brand + ' ' + self.model

class Vehicle(models.Model):

    model_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    brand = models.CharField(max_length= 200)
    model = models.CharField(max_length= 400)
    fuelType = models.CharField(max_length= 100)
    tireSpecs = models.CharField(max_length=10)
    tireWidth = models.IntegerField()
    tireHeight = models.IntegerField()
    rimSize = models.IntegerField()

    def __str__(self):
        return self.brand + ' ' + self.model

class User(models.Model):

    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length= 20)
    email = models.CharField(max_length= 100)
    password = models.CharField(max_length= 20)
    model_id = models.IntegerField(null = True, blank = True)
    
    def __str__(self):
        return self.email