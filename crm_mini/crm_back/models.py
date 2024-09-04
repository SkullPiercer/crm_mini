from django.db import models

class Group(models.Model):
    date = models.DateField(auto_now=True)
    time = models.TimeField()


class Student(models.Model):
    RECOMMENDED_GROUP_CHOICES = [
        ('junior', 'Младшая'),
        ('middle', 'Средняя'),
        ('senior', 'Старшая'),
    ]

    RECOMMENDED_DIRECTION_CHOICES = [
        ('sisters', 'Sisters'),
        ('it', 'IT'),
    ]

    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    description = models.TextField()
    recommended_direction = models.CharField(
        max_length=10,
        choices=RECOMMENDED_DIRECTION_CHOICES,
        default='sisters'
    )
    recommended_group = models.CharField(
        max_length=10,
        choices=RECOMMENDED_GROUP_CHOICES,
        default='junior'
    )
    responsiveness = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 11)],
        default=1
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


