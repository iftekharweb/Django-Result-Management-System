from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

@api_view(['GET'])
def get_students(request):
    return Response('OK')

@api_view(['GET'])
def test_home(request):
    return render(request,'test.html')
