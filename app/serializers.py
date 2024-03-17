from . import models
from rest_framework import serializers
from decimal import Decimal

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
    

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marks
        fields = '__all__'


# TRYING

class StudentResultSerializer(serializers.ModelSerializer):
    marks = MarkSerializer(many=True, source='marks_set')

    class Meta:
        model = models.Student
        fields = ['id', 'name', 'marks','semester_result']
    semester_result = serializers.SerializerMethodField(method_name='get_semester_result')

    def get_semester_result(self, obj):
        marks = obj.marks_set.all()
        total_marks = 0
        total_credits = 0
        
        for mark in marks:
            # ..
            HAVE_MARKS = Decimal(mark.attendence_marks)+Decimal(mark.ct_marks)+Decimal(mark.presentation_marks)+Decimal(mark.semester_final_marks)
            TOTAL_MARKS = 100/Decimal(mark.course.credits)
            PERCENT = (HAVE_MARKS/TOTAL_MARKS)*Decimal(100)
            GRADE = 0
            if PERCENT<40:
                GRADE = 0
            elif PERCENT<45:
                GRADE = 2.00
            elif PERCENT<50:
                GRADE = 2.25
            elif PERCENT<55:
                GRADE = 2.50
            elif PERCENT<60:
                GRADE = 2.75
            elif PERCENT<65:
                GRADE = 3.00
            elif PERCENT<70:
                GRADE = 3.25
            elif PERCENT<75:
                GRADE = 3.50
            elif PERCENT<80:
                GRADE = 3.75
            else:
                GRADE = 4.00
            # ..
            total_marks += Decimal(GRADE) * Decimal(mark.course.credits)
            total_credits += Decimal(mark.course.credits)
        
        print(total_marks)
        print(total_credits)
        
        # Calculate the semester result
        if total_credits > 0:
            semester_result = total_marks / total_credits
        else:
            semester_result = 0
        
        return semester_result

    


    
    
