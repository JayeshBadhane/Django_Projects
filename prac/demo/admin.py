from django.contrib import admin
# admin.py

from demo.models import Question, Choice, Department, Employees, Student

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Department)
admin.site.register(Employees)
admin.site.register(Student)
# Register your models here.
