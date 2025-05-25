from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30)
    date_joined = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)  # Present, Absent, Leave

    def __str__(self):
        return f"{self.employee} - {self.date} - {self.status}"

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    rating = models.IntegerField()  # 1 to 5
    feedback = models.TextField()

    def __str__(self):
        return f"{self.employee} - {self.month}"
