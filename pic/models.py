from django.db import models

# Create your models here.
class Emenities(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
         return self.name

class Gas(models.Models):
    pump_name = models.CharField(max_length=100)
    pump_address = models.TextField()
    price = models.IntegerField()
    pump_distance = models.IntegerField()
    pump_image = models.CharField(max_length=500)
    emenities = models.ManyToManyField(Emenities)

    def __str__(self):
        return self.pump_name