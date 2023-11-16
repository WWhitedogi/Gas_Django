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
    id = models.AutoField(primary_key=True)
    time = models.CharField(max_length=18)
    methane_ppm = models.FloatField()  # Methane concentration, stored as a FloatField
    formaldehyde_ppm = models.FloatField()  # Formaldehyde concentration, stored as a FloatField
    temperature = models.FloatField()  # Temperature, stored as a FloatField
    # humidity = models.FloatField()  # Humidity, stored as a FloatField

# class Sensorread(models.Model):
#     time = models.CharField(max_length=18, primary_key=True)
#     mvol = models.FloatField()  # Methane concentration, stored as a FloatField
#     mppm = models.FloatField()  # Methane concentration, stored as a FloatField
#     fvol = models.FloatField()  # Methane concentration, stored as a FloatField
#     fppm = models.FloatField()  # Formaldehyde concentration, stored asxs a FloatField
#     temp = models.IntegerField()  # Temperature, stored as a FloatField
#     humd = models.IntegerField()  # Humidity, stored as a FloatField