from django.db import models
from django.conf import settings


class Nutrition(models.Model):
    name = models.CharField(max_length=100, unique=True)

    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()

    def __str__(self):
        return self.name


class LogFood(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food = models.ForeignKey(Nutrition, on_delete=models.CASCADE)

    grams = models.FloatField()

    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()

    meal_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.food.name}"
