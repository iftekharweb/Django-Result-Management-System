from datetime import date
from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_COICE = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
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
    student_name = models.CharField(max_length=255)
    student_roll = models.IntegerField(unique=True)
    student_reg = models.DateField(unique=True)
    student_hall = models.CharField(max_length=255)
    student_session = models.CharField(max_length=100)

    student_email = models.EmailField()
    student_gender = models.CharField(max_length=8, choices=GENDER_COICE)
    student_date_of_birth = models.DateField(default=date.today())
    student_blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICE)
    student_address = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.student_roll} | {self.student_name}'

    

