from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_home),
    path('students/', views.get_students),
]