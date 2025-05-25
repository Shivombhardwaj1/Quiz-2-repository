# Import viewset and filtering tools from DRF and django-filter
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

# Import the models to expose via API
from .models import Employee, Attendance, Performance

# Import the corresponding serializers for each model
from .serializers import EmployeeSerializer, AttendanceSerializer, PerformanceSerializer


# ViewSet for Employee model
class EmployeeViewSet(viewsets.ModelViewSet):
    # Define the queryset for all Employee records
    queryset = Employee.objects.all()
    # Use the serializer that defines how Employee data is converted to/from JSON
    serializer_class = EmployeeSerializer

    # Enable filtering and search
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    # Allow filtering by department or role (make sure these fields exist in your model)
    filterset_fields = ['department', 'role']

    # Allow search by employee name, email, or phone
    search_fields = ['first_name', 'last_name', 'email', 'phone']


# ViewSet for Attendance model
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    # Enable filtering by status (e.g. Present/Absent) or date
    filterset_fields = ['status', 'date']

    # Enable search based on related employee's name
    search_fields = ['employee__first_name', 'employee__last_name']


# ViewSet for Performance model
class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    # Enable filtering by performance month or rating
    filterset_fields = ['month', 'rating']

    # Enable search based on related employee's name
    search_fields = ['employee__first_name', 'employee__last_name']
