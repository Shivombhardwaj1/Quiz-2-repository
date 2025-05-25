from django.db import models

# Employee model to store core employee details
class Employee(models.Model):
    first_name = models.CharField(max_length=50)  # Employee's first name
    last_name = models.CharField(max_length=50)   # Employee's last name
    department = models.CharField(max_length=50)  # Department name (e.g., HR, Engineering)
    role = models.CharField(max_length=50)        # Job role or title
    email = models.EmailField(unique=True)        # Unique email for each employee
    phone = models.CharField(max_length=30)       # Contact number
    date_joined = models.DateField()              # Date the employee joined
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # Employee's salary

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # Display full name in admin/panels

# Attendance model to track daily attendance of employees
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Linked employee
    date = models.DateField()                                         # Date of attendance
    status = models.CharField(max_length=10)  # Status like "Present", "Absent", or "Leave"

    def __str__(self):
        return f"{self.employee} - {self.date} - {self.status}"  # Display useful summary

# Performance model to record monthly performance ratings and feedback
class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Linked employee
    month = models.CharField(max_length=20)  # e.g., "January 2025"
    rating = models.IntegerField()           # Rating between 1 (low) to 5 (high)
    feedback = models.TextField()            # Optional textual feedback

    def __str__(self):
        return f"{self.employee} - {self.month}"  # Helps identify record by employee/month
