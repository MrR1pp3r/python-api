from django.db import models

# Create your models here.


class Student(models.Model):
    studentName = models.CharField(max_length=120)
    studentRoll = models.IntegerField()
    studentAge = models.IntegerField()
    studentUID = models.IntegerField()


class Course(models.Model):
    courseName = models.CharField(max_length=120)
    courseId = models.IntegerField()
    courseUId = models.IntegerField()
