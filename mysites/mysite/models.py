from django.db import models

# Create your models here.
class Rock(models.Model):
    Name=models.CharField(max_length=50)
    Music=models.CharField(max_length=50)
    Producer=models.CharField(max_length=50)
    Music_review=models.TextField()

class Traditional(models.Model):
    Name=models.CharField(max_length=50)
    Music=models.CharField(max_length=50)
    Producer=models.CharField(max_length=50)
    Music_review=models.TextField()

class Jazz(models.Model):
    Name=models.CharField(max_length=50)
    Music=models.CharField(max_length=50)
    Producer=models.CharField(max_length=50)
    Music_review=models.TextField()

class Pop(models.Model):
    Name=models.CharField(max_length=50)
    Music=models.CharField(max_length=50)
    Producer=models.CharField(max_length=50)
    Music_review=models.TextField()

    