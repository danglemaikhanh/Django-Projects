from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


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
    assigned_to = models.ManyToManyField(TeamMember)


class TimeEntry(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    start_at = models.DateTimeField()
    duration = models.IntegerField()
    description = models.TextField()
