from django.contrib import admin
from . import models


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'id_no',
        'first_name',
        'last_name',
        'email'
    ]
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['id_no']

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
    readonly_fields = ['semester_result']

@admin.register(models.Mark)
class MarksAdmin(admin.ModelAdmin):
    list_display = [
        'student',
        'semester',
        'course',
        'section',
        'attendence_marks',
        'ct_marks',
        'presentation_marks',
        'semester_final_marks'
    ]
    list_editable = [
        'attendence_marks',
        'ct_marks',
        'presentation_marks',
        'semester_final_marks'
    ]
    search_fields = [
        'student__id_no',
        'semester__title',
    ]

