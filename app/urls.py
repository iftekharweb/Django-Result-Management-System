from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('students', views.StudentViewSet, basename='students')

urlpatterns = router.urls