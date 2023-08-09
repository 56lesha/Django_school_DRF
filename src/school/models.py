from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return self.lastname


class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name