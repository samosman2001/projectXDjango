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
	# 	return self.name
class WorkoutLogs(models.Model):
	MODE_CHOICES = [
	("gym","Gym"),
	("home","Home")
	]	
	user = models.ForeignKey(Exercise,on_delete  = models.PROTECT,related_name = "logs")
	logged_at = models.DateTimeField()

	mode = models.CharField(
       max_length = 10,
       choices = MODE_CHOICES,
       default = "gym"
		)

	sets = models.PositiveIntegerField(default = 0)
	reps = models.PositiveIntegerField(default = 0)
	weight_kg = models.FloatField(null = True,blank = True)

	duration_min = models.PositiveIntegerField(default = 0)
	calories_burned = models.PositiveIntegerField(default = 0)
	created_at = models.DateTimeField(auto_now_add = True)
	





