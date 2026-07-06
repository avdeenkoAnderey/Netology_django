from django.conf import settings
from django.db import models


class Advertisement(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Открыто'),
        ('CLOSED', 'Закрыто'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='OPEN',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='advertisements')

    def __str__(self):
        return self.title
