from django.db import models
from django.conf import settings

class Exercise(models.Model):
	MODE_CHOICES = [
	("gym","Gym"),
	("home","Home")
	]

	name = models.CharField(max_length = 120,unique = True)

	mode = models.CharField(max_length = 10,choices = MODE_CHOICES,default ="Gym")

	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add = True)

	# def __str__(self):
	# 	return self.namea
class WorkoutLog(models.Model):
	MODE_CHOICES = [
	("gym","Gym"),
	("home","Home")
	]	
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	mode = models.CharField(
       max_length = 10,
       choices = MODE_CHOICES,
       default = "gym"
		)
	name = models.CharField(max_length = 100)
	sets = models.PositiveIntegerField(default = 0)
	reps = models.PositiveIntegerField(default = 0)
	seconds = models.PositiveIntegerField(default= 0)
	weight_kg = models.FloatField(null = True,blank = True)
	calories = models.FloatField(default= 0.0)
	created_at = models.DateTimeField(auto_now_add = True)


class WorkoutPlan(models.Model):
    MODE_CHOICES = [("gym", "Gym"), ("home", "Home")]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="workout_plans"
    )

    name = models.CharField(max_length=120)
    mode = models.CharField(max_length=10, choices=MODE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.mode})"


class WorkoutPlanExercise(models.Model):
    plan = models.ForeignKey(
        WorkoutPlan,
        on_delete=models.CASCADE,
        related_name="exercises"
    )

    exercise_name = models.CharField(max_length=120)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.exercise_name}"


class WorkoutPlanSet(models.Model):
    plan_exercise = models.ForeignKey(
        WorkoutPlanExercise,
        on_delete=models.CASCADE,
        related_name="sets"
    )

    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.FloatField(default=0)
    status = models.CharField(max_length=40, blank=True)
    mode = models.CharField(max_length=10, choices=[("gym","Gym"),("home","Home")])

    def __str__(self):
        return f"{self.sets}x{self.reps} ({self.weight}kg)"

	





