from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=300)
    message=models.CharField(max_length=1000)

class Team(models.Model):
    img=models.ImageField(upload_to='profile')
    name=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    discription=models.TextField(max_length=2000)

