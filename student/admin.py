from django.contrib import admin
from student.models import StudentInfo
# Register your models here.


@admin.register(StudentInfo)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','mobile_number','email','address']