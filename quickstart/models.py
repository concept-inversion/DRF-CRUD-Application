from django.db import models

# Create your models here.
class Personal(models.Model):
    Name = models.CharField(max_length=255)
    Address = models.TextField()
    PhoneNo = models.IntegerField()
    
