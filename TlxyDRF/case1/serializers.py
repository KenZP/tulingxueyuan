from rest_framework import serializers
from case1.models import *

class StudentSer(serializers.ModelSerializer):
	"""docstring for StudentSer"""
	class Meta:
		"""docstring for Meta"""
		model = Student
		fielders = '__all__'
		
			
