from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth import get_user_model


class User(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

User = get_user_model()


class Feedback(models.Model):
    SENTIMENT_CHOICES = [
        ('positive', 'Positive'),
        ('neutral', 'Neutral'),
        ('negative', 'Negative'),
    ]

    strengths = models.TextField()
    areas_to_improve = models.TextField()
    sentiment = models.CharField(max_length=10, choices=SENTIMENT_CHOICES)
    created_by = models.ForeignKey(User, related_name='given_feedbacks', on_delete=models.CASCADE)
    created_for = models.ForeignKey(User, related_name='received_feedbacks', on_delete=models.CASCADE)
    employee_comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    acknowledged = models.BooleanField(default=False)

    def __str__(self):
        return f"Feedback for {self.created_for.username} by {self.created_by.username}"

