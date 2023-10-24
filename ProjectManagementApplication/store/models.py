from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_at = models.DateTimeField()

    PRIORITY_CHOICES = (
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    )
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="low")
    assigned_to = models.ManyToManyField(User, through="TeamMember")


class TeamMember(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TimeEntry(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    start_at = models.DateTimeField()
    duration = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
