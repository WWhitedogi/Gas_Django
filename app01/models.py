from django.db import models

# Create your models here.
class Admin(models.Model):
    """Manager"""
    username=models.CharField(verbose_name="username",max_length=32)
    password=models.CharField(verbose_name="password",max_length=64)
    def __str__(self):
        return self.username

class UserInfo(models.Model):
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    age=models.IntegerField

class Measurement(models.Model):
    methane_concentration = models.FloatField()  # Methane concentration, stored as a FloatField
    formaldehyde_concentration = models.FloatField()  # Formaldehyde concentration, stored as a FloatField
    temperature = models.FloatField()  # Temperature, stored as a FloatField
    humidity = models.FloatField()  # Humidity, stored as a FloatField
