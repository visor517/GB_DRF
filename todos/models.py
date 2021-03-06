from django.db import models

from users.models import User


class Project(models.Model):
    STATUSES = (
        ('OPEN', 'открыт'),     # есть открытые туду
        ('DONE', 'сделан'),     # все туду закрыты
    )

    name = models.CharField(max_length=128)
    description = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    authors = models.ManyToManyField(User)
    status = models.CharField(choices=STATUSES, default='OPEN', max_length=4)

    def __str__(self):
        return f'{self.name}'


class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.project.name} - {self.name}'
