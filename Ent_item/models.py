from django.db import models

# Create your models here.

class Student(models.Model):
    s_name = models.CharField(max_length=50)
    s_class = models.IntegerField()
    s_address = models.CharField(max_length=50)
    