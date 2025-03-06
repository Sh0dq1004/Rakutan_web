from django.db import models

# Create your models here.
class subject(models.Model):
    name=models.CharField(max_length=32)
    teaher=models.CharField(max_length=16)
    grade=models.IntegerField()
    term=models.IntegerField()
    major=models.CharField(max_length=8)
    eval=models.IntegerField()