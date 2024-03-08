from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render


def get_students(request):
    return render(request, 'hello.html')


def test_home(request):
    return render(request,'test.html')
