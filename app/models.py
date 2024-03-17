from django.db import models
from django.conf import settings
from django.contrib import admin


class Semester(models.Model): 
    semester_no = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    students = models.ManyToManyField(
        'Student', 
        null=True, 
        related_name='+',
        blank=True
    )
    courses = models.ManyToManyField(
        'Course', 
        related_name='+', 
        null=True,
        blank=True
        )
    def __str__(self) -> str:
        return self.title

class Teacher(models.Model):
    id_no = models.CharField(max_length=255)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    def email(self):
        return self.user.email
    
    class Meta:
        ordering = ['user__first_name', 'user__last_name', 'id_no']

class Course(models.Model):
    course_code = models.CharField(
        max_length=20, 
        unique=True
    )
    title = models.CharField(max_length=255)
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT)
    sectionA_assigned_teacher = models.ForeignKey(
        Teacher, 
        on_delete=models.SET_NULL, 
        null=True,  
        related_name='sectionA_courses'
    )
    sectionB_assigned_teacher = models.ForeignKey(
        Teacher, 
        related_name='sectionB_courses', 
        on_delete=models.SET_NULL, 
        null=True
    )
    credits = models.IntegerField()
    def __str__(self) -> str:
        return f'{self.course_code} - {self.title}'

class Student(models.Model):
    BLOOD_GROUP_CHOICE = [
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('O-', 'O-'),
    ]
    name = models.CharField(max_length=255)
    id_no = models.CharField(max_length=20, unique=True)
    hsc_reg = models.CharField(max_length=20, unique=True)
    university = models.CharField(max_length=255, default='University of Rajshahi')
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP_CHOICE)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True)
    session = models.CharField(max_length=20, default='2018-2019')
    birth_day = models.DateField()
    residential_hall_name = models.CharField(max_length=255)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    semester_result = models.DecimalField(max_digits=5, decimal_places=3)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.id_no}'


class Mark(models.Model):
    SECTION_CHOICES = [
        ('A', 'Section A'),
        ('B', 'Section B'),
        ('L', 'LAB')
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.CharField(max_length=1, choices=SECTION_CHOICES)

    attendence_marks = models.DecimalField(max_digits=5, decimal_places=2)
    ct_marks = models.DecimalField(max_digits=5, decimal_places=2)
    presentation_marks = models.DecimalField(max_digits=5, decimal_places=2)
    semester_final_marks = models.DecimalField(max_digits=5, decimal_places=2)

class SemesterCGPA(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    scgpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True)



class YearlyCGPA(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    year = models.IntegerField()
    ycgpa = models.DecimalField(max_digits=5, decimal_places=2)
