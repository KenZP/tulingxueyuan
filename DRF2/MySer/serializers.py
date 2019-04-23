from rest_framework import serializers

class StudentSerializer(serializers.Serializer):

	'''
	里面写的是每一个需要序列化/反序列化的字段
	跟定义模型基本一致
	'''
	name = serializers.CharField(label='姓名', max_length=20)
	age = serializers.IntegerField()
	score = serializers.IntegerField()

	