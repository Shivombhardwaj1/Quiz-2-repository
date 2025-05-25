from django.core.management.base import BaseCommand
from faker import Faker
from employee.models import Employee, Attendance, Performance
import random

class Command(BaseCommand):
    help = 'Seed the database with fake employee data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(5):
            employee = Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                department=random.choice(['HR', 'Engineering', 'Sales']),
                role=random.choice(['Developer', 'Manager', 'Analyst']),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                date_joined=fake.date_between(start_date='-2y', end_date='today'),
                salary=round(random.uniform(30000, 100000), 2)
            )

            for _ in range(10):
                Attendance.objects.create(
                    employee=employee,
                    date=fake.date_between(start_date='-2m', end_date='today'),
                    status=random.choice(['Present', 'Absent', 'Leave'])
                )

            for _ in range(3):
                Performance.objects.create(
                    employee=employee,
                    month=fake.month_name(),
                    rating=random.randint(1, 5),
                    feedback=fake.sentence()
                )

        self.stdout.write(self.style.SUCCESS('Seeded database with employee data.'))
