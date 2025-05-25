# Employee Data API

This project is a Django REST Framework-based API for managing and analyzing employee data.

## Features

- Synthetic data generation with Faker
- PostgreSQL integration
- REST APIs with search, filter, and pagination
- Swagger UI for documentation
- Token Authentication

  
---------------------------------------Example if you want to use get api for above features------------------

Filter employees by department:
/api/employees/?department=Sales

Search employees by name or email:
/api/employees/?search=john

Pagination (if enabled, default page size 10):
/api/employees/?page=2

Filter attendance by status:
/api/attendance/?status=Present

Search attendance by employee name:
/api/attendance/?search=smith

Filter performance by month:
/api/performance/?month=May 2023

-----------------------------------------------------## Setup Instructions-------------------------------------------------------

1. Clone the repo:

```bash
git clone using my repo
cd employee-project


