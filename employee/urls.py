# Import necessary URL and view components
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import the viewsets that handle API logic
from .views import EmployeeViewSet, AttendanceViewSet, PerformanceViewSet

# Initialize a DefaultRouter which will automatically create RESTful routes
router = DefaultRouter()

# Register viewsets with the router
# This sets up routes like:
# - /employees/
# - /employees/{id}/
# - /attendance/
# - /performance/
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'attendance', AttendanceViewSet, basename='attendance')
router.register(r'performance', PerformanceViewSet, basename='performance')

# Include the router-generated URL patterns into this app's URLconf
urlpatterns = [
    path('', include(router.urls)),
]
