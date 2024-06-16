from django.db import models

class Class(models.Model):
    name  = models.CharField(max_length = 20)
    color = models.CharField(max_length = 20)
    building_material = models.CharField(max_length = 20)
    size= models.CharField(max_length = 20)
    capacity = models.PositiveBigIntegerField()
    lighting = models.CharField(max_length = 100)
    temeprature = models.PositiveSmallIntegerField()
    odor = models.CharField(max_length = 20)
    comfort = models.CharField(max_length = 20)
    state = models.CharField(max_length = 20)



    def __str__(self):
        return f"{self.name} {self.capacity}"