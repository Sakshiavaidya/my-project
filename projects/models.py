from django.db import models
from django.contrib.auth.models import User
from clients.models import Client

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='projects_created', on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name
