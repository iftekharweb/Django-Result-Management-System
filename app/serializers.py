from . import models
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = [
            'id',
            'name',
            'id_no',
            'hsc_reg',
            'university',
            'blood_group',
            'email',
            'phone_number',
            'session',
            'birth_day',
            'residential_hall_name'
        ]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = [
            'id',
            'course_code', 
            'title', 
            'sectionA_assigned_teacher',
            'sectionB_assigned_teacher',
            'credits'
            ]



class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Teacher
        fields = ['id','name', 'email', 'sectionA_courses', 'sectionB_courses']

        sectionA_courses = serializers.PrimaryKeyRelatedField(
            queryset=models.Course.objects.all()
        )
        sectionB_courses = serializers.PrimaryKeyRelatedField(
            queryset=models.Course.objects.all()
        )
    
    
