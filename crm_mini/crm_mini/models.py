from django.db import models

class Group(models.Model):
    date = models.DateField(auto_now=True)
    time = models.TimeField()


class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    description = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


