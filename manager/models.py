from django.db import models

# Create your models here.
class tire1_class(models.Model):
    name=models.CharField(max_length=64)
    teaher=models.CharField(max_length=64)
    term=models.CharField(max_length=16)
    grade=models.CharField(max_length=8)
    major=models.CharField(max_length=16)

class tire2_class(models.Model):
    name=models.CharField(max_length=64)
    teaher=models.CharField(max_length=64)
    term=models.CharField(max_length=16)
    grade=models.CharField(max_length=8)
    major=models.CharField(max_length=16)
