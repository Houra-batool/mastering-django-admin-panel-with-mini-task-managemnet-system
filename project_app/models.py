from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'TO DO'),
        ('IN_PROGRESS', 'IN PROGRESS'),
        ('DONE', 'DONE'),
        ('PENDING', 'PENDING'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks')

    def __str__(self):
        return self.title
