# from rest_framework import serializers
# from . import models
# from ..app.serializers import StudentSerializer as SS
# from ..app.models import Student as S

# class SemesterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Semester
#         fields = ['id', 'semester_number', 'semester_name']

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Student
#         fields = ['id', 'srudent_details']
    
#     srudent_details = serializers.SerializerMethodField(method_name='get_details')

#     def get_details(self, obj):
#         detail =S.objects.filter(sectionA_assigned_teacher=obj)
#         detail_serializer = SS(detail, many=True)
#         return detail_serializer.data
    
#     def create(self, validated_data):
#         student_id = self.context['student_id']
#         return models.Student.objects.create(student_id=student_id, **validated_data) 