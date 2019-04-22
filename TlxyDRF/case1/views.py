from django.shortcuts import render

from rest_framework import viewsets

from case1.serializers import *
from case1.models import Student
# Create your views here.



class StudentVS(viewsets.ModelViewSet):
	"""docstring for StudentVS"""
	serializer_class = StudentSer
	queryset = Student.objects.all()
		