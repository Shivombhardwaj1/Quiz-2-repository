from django.core.management.base import BaseCommand
from faker import Faker
from employee.models import Employee, Attendance, Performance
import random

class Command(BaseCommand):
    # Help message for the management command
    help = 'Seed the database with fake employee data'

    def handle(self, *args, **kwargs):
        fake = Faker()  # Initialize Faker instance for generating fake data

        # Generate data for 5 employees
        for _ in range(5):
            # Create a fake employee
            employee = Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                department=random.choice(['HR', 'Engineering', 'Sales']),  # Random department
                role=random.choice(['Developer', 'Manager', 'Analyst']),  # Random job role
                email=fake.unique.email(),
                phone=fake.phone_number(),
                date_joined=fake.date_between(start_date='-2y', end_date='today'),  # Within last 2 years
                salary=round(random.uniform(30000, 100000), 2)  # Salary between 30k and 100k
            )

            # Create 10 attendance records for the employee
            for _ in range(10):
                Attendance.objects.create(
                    employee=employee,
                    date=fake.date_between(start_date='-2m', end_date='today'),  # From past 2 months
                    status=random.choice(['Present', 'Absent', 'Leave'])  # Random status
                )

            # Create 3 performance records for the employee
            for _ in range(3):
                Performance.objects.create(
                    employee=employee,
                    month=fake.month_name(),  # Random month name
                    rating=random.randint(1, 5),  # Rating from 1 to 5
                    feedback=fake.sentence()  # Random feedback sentence
                )

        # Success message after seeding
        self.stdout.write(self.style.SUCCESS('✅ Seeded database with employee data.'))
