from rest_framework import serializers
from .models import Employee, Attendance, Performance

# Serializer for the Employee model
# Converts Employee model instances to/from JSON
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'  # Include all fields in the Employee model


# Serializer for the Attendance model
# Used to represent attendance records in the API
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'  # Include all fields in the Attendance model


# Serializer for the Performance model
# Used to represent performance data in the API
class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'  # Include all fields in the Performance model
