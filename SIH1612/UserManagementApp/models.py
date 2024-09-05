from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Defining roles
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('planner', 'Planner'),
        ('scheduler', 'Scheduler'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # Avoid conflicts with groups and permissions by setting related_name
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Add a related_name to avoid conflicts
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Add a related_name to avoid conflicts
        blank=True
    )

    def __str__(self):
        return self.username
