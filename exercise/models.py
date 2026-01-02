from django.db import models



class Exercise(models.Model):
	name = models.CharField(max_length = 120)
	muscle_group = models.CharField(max_length = 120,blank = True )


