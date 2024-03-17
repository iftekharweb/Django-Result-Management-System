from rest_framework import generics
from rest_framework import viewsets
from . import models, serializers
from rest_framework import generics

class SemesterViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return models.Semester.objects.all()
    
    def get_serializer_class(self):
        return serializers.SemesterSerializer


class StudentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return models.Student.objects.all()
    
    def get_serializer_class(self):
        return serializers.StudentSerializer
    
class TeacherViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return models.Teacher.objects.all()
    
    def get_serializer_class(self):
        return serializers.TeacherSerializer
    
class CourseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return models.Course.objects.all()
    
    def get_serializer_class(self):
        return serializers.CourseSerializer
    

class MarkViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return models.Mark.objects.all()
    
    def get_serializer_class(self):
        return serializers.MarkSerializer
    

# TRYING

class StudentResultView(generics.RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentResultSerializer


