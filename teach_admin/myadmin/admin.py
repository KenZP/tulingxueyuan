from django.contrib import admin

from myadmin.models import *
# Register your models here.

admin.site.site_header = "这是站头"
admin.site.site_title = "这是站标题"
admin.site.index_title = "首页标题"

class ClassRoomAdmin(admin.ModelAdmin):
	"""docstring for Admininfo"""
	pass


class TeacherAdmin(admin.ModelAdmin):
	"""docstring for TeacherAdmin"""
	list_per_page = 2
	actions_on_bottom = True
	actions_on_top = False
	list_display = ["name","room","curTime","getRoomName"]

	search_fields = ["name"]# 按什么搜索的搜索框

	#fields = ["name","course"]# 需要显示的老师的信息

	fieldsets = (
		("基本信息", {"fields":["name",]}),
		("其他信息", {"fields":["room","course"]}),
		)
		
#@admin.site.register(Student)		
class StudentAdmin(admin.ModelAdmin):
	"""docstring for TeacherAdmin"""
	pass

admin.site.register(ClassRoom,ClassRoomAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)



# admin.site.register(ClassRoom)
# admin.site.register(Teacher)
# admin.site.register(Student)