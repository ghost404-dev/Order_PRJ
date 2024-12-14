from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('in_progress', 'В работе'),
        ('completed','Завершён'),
        ('cancelled','Отменён'),
    ]
    
    project_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    client = models.CharField(max_length=255)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project_name} - {self.status}"


class UserActivityLog(models.Model):
    ACTION_CHOICES = [
        ('LOGIN', 'Вошел'),
        ('LOGOUT', 'Вышел'),
        ('CREATE', 'Создал'),
        ('UPDATE', 'Обновил'),
        ('DELETE', 'Удалил'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    object_type = models.CharField(max_length=50, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.action} - {self.timestamp}'
