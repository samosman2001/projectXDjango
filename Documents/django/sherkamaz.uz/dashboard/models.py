from django.db import models
from django.contrib.auth.models import User   # optional, if you relate to Django users
from datetime import datetime

class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sets = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    status = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField()
    created_at = models.DateField(default = datetime.now)
    mode = models.CharField(max_length=10, choices=[('gym', 'Gym'), ('home', 'Home')], default='gym')
    streak = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.mode})"


class Users(models.Model):
    email = models.CharField(max_length = 100)
    password = models.CharField(default = datetime.now,max_length = 100)
    created_at = models.DateField(default = datetime.now)
    password_hash = models.CharField(default = "",max_length=100)
    remember_token = models.CharField(default = "",max_length = 100)
    

class Admin(Users):

    advancedCalorieTable = models.FloatField(default = 0)

  
class regularUser(Users):

    streak = models.IntegerField(default = 0)
    weight_kg = models.FloatField(default = 0)
    heigh_cm = models.FloatField(default = 0)
    last_logged = models.DateField(default = datetime.now)

