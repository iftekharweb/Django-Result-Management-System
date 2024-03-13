from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from . import models, serializers

class StudentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return models.Student.objects.all()
    
    def get_serializer_class(self):
        return serializers.StudentSerializer


