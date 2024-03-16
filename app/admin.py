from django.contrib import admin
from . import models


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'id_no',
        'name',
        'email'
    ]
    search_fields = ['id_no', 'name']

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'course_code',
        'title',
        'semester',
        'sectionA_assigned_teacher',
        'sectionB_assigned_teacher',
        'credits'
    ]
    search_fields = ['course_code']

@admin.register(models.Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = [
        'semester_no',
        'title'
    ]
    search_fields = ['semester_no','title']

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'id_no',
        'name',
        'semester',
        'session'
    ]
    list_editable = ['semester']
    search_fields = ['id_no', 'semester', 'session']

