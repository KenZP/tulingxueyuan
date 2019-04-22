from django.db import models

# Create your models here.


class ClassRoom(models.Model):
	roomName = models.CharField(max_length=20)
	Loc = models.CharField(max_length=20)

class Student(models.Model):
	"""docstring for Student"""
	name = models.CharField(max_length=20)
	age = models.IntegerField()

class Teacher(models.Model):
	"""docstring for Teacher"""
	course = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	age = models.IntegerField()
	
		
		