from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    tel = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    class Meta:
        abstract = True

class Teacher(Person):
    speciality = models.CharField(max_length=50)
    def __str__(self):
        speciality = str(self.speciality)
        return self.first_name + " " + self.last_name +" "+ self.birth_date + " " + self.tel + " " + self.email + " " + self.speciality



class Student(Person):
    pathway = models.CharField(max_length=50)
    def __str__(self):
        pathway = str(self.pathway)
        return self.first_name + " " + self.last_name +" "+ self.birth_date + " " + self.tel + " " + self.email + " " + self.pathway