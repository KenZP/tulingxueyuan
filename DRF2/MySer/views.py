from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.views import APIView

from MySer.models import Student
from MySer.serializers import StudentSerializer

from rest_framework.generics import GenericAPIView

from rest_framework.viewsets import ModelViewSet


class StudentGenericAPIView(GenericAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	def get(self, request):
		ser = self.get_serializer(self.queryset.all(), many=True)
		return Response(data=ser.data)



class StudentVS(viewsets.ModelViewSet):
	serializer_class = StudentSerializer
	queryset = Student.objects.all()

	print("hahahaha")

	def list(self, request,*args, **kwargs):
		rst = super(StudentVS,self).list(*args, **kwargs)
		return rst


class StudentAPIView(APIView):
	'''
	处理用户的get请求
	'''

	def get(self, request):
		stus = Student.objects.all()
		ser = StudentSerializer(stus,many=True)
		return Response(data=ser.data)
		
