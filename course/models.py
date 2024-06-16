from django.db import models

class Course(models.Model):
    course_name  = models.CharField(max_length = 20)
    trainer_name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 100)
    level= models.CharField(max_length = 20)
    duration = models.PositiveBigIntegerField()
    objective = models.CharField(max_length = 100)
    module = models.PositiveSmallIntegerField()
    prior_needed_skills= models.CharField(max_length = 20)
    learning_materials = models.CharField(max_length = 20)
    attendance_per_week = models.PositiveSmallIntegerField()



    def __str__(self):
        return f"{self.course_name} {self.duration}"