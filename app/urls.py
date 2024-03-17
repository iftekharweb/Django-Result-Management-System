from rest_framework_nested import routers
from django.urls import path, include
from . import views


router = routers.DefaultRouter()
router.register('students', views.StudentViewSet, basename='students')
router.register('teachers', views.TeacherViewSet, basename='teachers')
router.register('courses', views.CourseViewSet, basename='courses')
router.register('semesters', views.SemesterViewSet, basename='semesters')
router.register('marks', views.MarkViewSet, basename='marks')

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
    path('students/<int:pk>/result/', views.StudentResultView.as_view(), name='student-result')
]