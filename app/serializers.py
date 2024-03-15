from . import models
from rest_framework import serializers

class CustomCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'title', 'course_code']

class CustomStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'name', 'id_no', 'session', 'residential_hall_name']

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Semester
        fields = [
            'id',
            'semester_no',
            'title',
            'have_students',
            'have_courses'
        ]
    have_students = serializers.SerializerMethodField(method_name='get_students')
    have_courses = serializers.SerializerMethodField(method_name='get_courses')

    def get_students(self, obj):
        students = models.Student.objects.filter(semester=obj)
        students_serializer = CustomStudentSerializer(students, many=True)
        return students_serializer.data

    def get_courses(self, obj):
        courses = models.Course.objects.filter(semester=obj)
        courses_serializer = CustomCourseSerializer(courses, many=True)
        return courses_serializer.data

    
    

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = [
            'id',
            'semester',
            'name',
            'id_no',
            'hsc_reg',
            'university',
            'blood_group',
            'email',
            'phone_number',
            'session',
            'birth_day',
            'residential_hall_name',

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


# /teachers 
# /teachers/<id>

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Teacher
        fields = ['id','name', 'email', 'section_As', 'section_Bs']
    
    section_As = serializers.SerializerMethodField(method_name='get_sectionA_sir')
    section_Bs = serializers.SerializerMethodField(method_name='get_sectionB_sir')

    def get_sectionA_sir(self, obj):
        sectionA_courses = models.Course.objects.filter(sectionA_assigned_teacher=obj)
        sectionA_serializer = CustomCourseSerializer(sectionA_courses, many=True)
        return sectionA_serializer.data
    
    def get_sectionB_sir(self, obj):
        sectionB_courses = models.Course.objects.filter(sectionB_assigned_teacher=obj)
        sectionB_serializer = CustomCourseSerializer(sectionB_courses, many=True)
        return sectionB_serializer.data
    


    
    
