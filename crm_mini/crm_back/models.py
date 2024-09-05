from django.db import models

class Group(models.Model):
    date = models.DateField(auto_now=True)
    time = models.TimeField()


class Student(models.Model):
    RECOMMENDED_GROUP_CHOICES = [
        ('junior', 'Младшая'),
        ('middle', 'Средняя'),
        ('senior', 'Старшая'),
        ('not selected', 'Не выбрано'),
    ]

    RECOMMENDED_DIRECTION_CHOICES = [
        ('sisters', 'Sisters'),
        ('it', 'IT'),
        ('not selected', 'Не выбрано'),
    ]

    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)
    recommended_direction = models.CharField(
        max_length=12,
        choices=RECOMMENDED_DIRECTION_CHOICES,
        default='Не выбрано',
        blank=True
    )
    recommended_group = models.CharField(
        max_length=12,
        choices=RECOMMENDED_GROUP_CHOICES,
        default='Не выбрано',
        blank=True
    )
    responsiveness = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 11)],
        default=1,
        blank=True
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    parents = models.TextField()
    manager_description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
