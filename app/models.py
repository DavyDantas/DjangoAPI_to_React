from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=150)
    grade1 = models.IntegerField()
    grade2 = models.IntegerField()
    average = models.IntegerField(blank=True, null=True)
    
    def calculateAverage(self):
        self.average = round((self.grade1 + self.grade2) /2)
        self.save()
        
    def __str__(self): 
        return self.name