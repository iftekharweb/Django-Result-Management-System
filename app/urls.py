from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('students', views.StudentViewSet, basename='students')
router.register('teachers', views.TeacherViewSet, basename='teachers')
router.register('courses', views.CourseViewSet, basename='courses')
router.register('semesters', views.SemesterViewSet, basename='semesters')

urlpatterns = router.urls