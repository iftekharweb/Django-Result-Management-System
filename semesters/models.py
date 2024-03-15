# from django.db import models
# from ..app import models as MM

# class Semester(models.Model):
#     semester_number = models.IntegerField(unique=True)
#     semester_name = models.CharField(max_length=255)
    

#     def __str__(self) -> str:
#         if self.semester_number == 1:
#             return f'1st Year Odd Semester'
#         elif self.semester_number == 2:
#             return f'1st Year Even Semester'
#         elif self.semester_number == 3:
#             return f'2nd Year Odd Semester'
#         elif self.semester_number == 4:
#             return f'2nd Year Even Semester'
#         elif self.semester_number == 5:
#             return f'3rd Year Odd Semester'
#         elif self.semester_number == 6:
#             return f'3rd Year Even Semester'
#         elif self.semester_number == 7:
#             return f'4th Year Odd Semester'
#         elif self.semester_number == 8:
#             return f'4th Year Even Semester'
        
# class Student(models.Model):
#     semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
#     student = models.ForeignKey(MM.Student, on_delete=models.PROTECT)
