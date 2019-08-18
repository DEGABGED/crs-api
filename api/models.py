from django.db import models

# Create your models here.

# Based on the CRS package model
class Subject(models.Model):
    class_code = models.CharField(max_length=10, primary_key=True)
    course = models.CharField(max_length=20, blank=True, default='')
    class_name = models.CharField(max_length=50)
    credits = models.FloatField(default=0.0)
    schedule = models.TextField() # To be changed later on
    instructor = models.CharField(max_length=50)
    remarks = models.TextField()
    slots_avail = models.IntegerField(default=0)
    slots_total = models.IntegerField(default=0)
    demand = models.IntegerField(default=0)
