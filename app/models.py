from django.db import models

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
    phone_number = models.CharField(max_length=15)
    session = models.CharField(max_length=20, default='2018-2019')
    birth_day = models.DateField()
    residential_hall_name = models.CharField(max_length=255)
    # Assuming result is a CharField storing JSON or similar structured data
    # result = models.JSONField()

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    sectionA_assigned_teacher = models.ForeignKey(Teacher, related_name='sectionA_courses', on_delete=models.SET_NULL, null=True)
    sectionB_assigned_teacher = models.ForeignKey(Teacher, related_name='sectionB_courses', on_delete=models.SET_NULL, null=True)
    credits = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.course_code} - {self.title}'
    


class Semester(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester_number = models.IntegerField()
    courses = models.ManyToManyField(Course)


class Marks(models.Model):
    SECTION_CHOICES = [
        ('A', 'Section A'),
        ('B', 'Section B'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.CharField(max_length=1, choices=SECTION_CHOICES)

    attendence_marks = models.DecimalField(max_digits=5, decimal_places=2)
    ct_marks = models.DecimalField(max_digits=5, decimal_places=2)
    presentation_marks = models.DecimalField(max_digits=5, decimal_places=2)
    semester_final_marks = models.DecimalField(max_digits=5, decimal_places=2)


class YearlyCGPA(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    year = models.IntegerField()
    ycgpa = models.DecimalField(max_digits=5, decimal_places=2)

class SemesterCGPA(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    scgpa = models.DecimalField(max_digits=5, decimal_places=2)
