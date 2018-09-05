from django.db import models

# Create your models here.
class Bus(models.Model):

    name=models.CharField(max_length=20)


    def __str__(self):

        return self.name

class String(models.Model):

    name=models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name