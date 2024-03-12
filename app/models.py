from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=150)
    grade1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    grade2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    average = models.IntegerField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.average = round((self.grade1 + self.grade2) /2)
        super(Student, self).save(*args, **kwargs)
        
    def __str__(self): 
        return self.name