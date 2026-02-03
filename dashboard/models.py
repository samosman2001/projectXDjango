from django.db import models
from django.contrib.auth.models import User   # optional, if you relate to Django users
from datetime import datetime

class UserMetrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    weight = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.age} - {self.weight}"
