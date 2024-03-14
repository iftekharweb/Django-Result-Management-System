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

class TeacherCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'title', 'course_code']

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Teacher
        fields = ['id','name', 'email', 'sectionA_sir', 'sectionB_sir']
    
    sectionA_sir = serializers.SerializerMethodField(method_name='get_sectionA_sir')
    sectionB_sir = serializers.SerializerMethodField(method_name='get_sectionB_sir')

    def get_sectionA_sir(self, obj):
        sectionA_courses = models.Course.objects.filter(sectionA_assigned_teacher=obj)
        sectionA_serializer = TeacherCourseSerializer(sectionA_courses, many=True)
        return sectionA_serializer.data
    
    def get_sectionB_sir(self, obj):
        sectionB_courses = models.Course.objects.filter(sectionB_assigned_teacher=obj)
        sectionB_serializer = TeacherCourseSerializer(sectionB_courses, many=True)
        return sectionB_serializer.data
    
    
