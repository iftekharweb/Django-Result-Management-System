from . import models
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = [
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