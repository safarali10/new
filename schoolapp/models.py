from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Course(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



# Create your models here.
