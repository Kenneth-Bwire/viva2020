from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    website = models.URLField()
    

    def __str__(self):
        return self.name

"""
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
"""
