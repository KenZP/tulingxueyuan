from rest_framework import serializers
from MySer.models import *


class StudentSerializer(serializers.Serializer):

	'''
	第一种方法：
	里面写的是每一个需要序列化/反序列化的字段
	跟定义模型基本一致
	'''
	# name = serializers.CharField(label='姓名', max_length=20)
	# age = serializers.IntegerField()
	# score = serializers.IntegerField()

    # 第二种方法：
	class Meta:
		model = Student     # 序列化对应的模型
		fields = '__all__'  # 把所有的属性都序列化


	