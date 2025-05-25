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

============================================================for attendance ==========================================================
You can now test like this:

 Pagination
GET http://localhost:8000/api/attendance/?page=2
 
 Filter (e.g., Present status)
GET http://localhost:8000/api/attendance/?status=Present

 Search (e.g., search by employee first name)
GET http://localhost:8000/api/attendance/?search=John

 Combined
GET http://localhost:8000/api/attendance/?status=Present&search=John&page=1

===========================================================to post request of attendance=================================================
POST Request to Mark Attendance

use POST /api/attendance/ 

with the following JSON body:
example-
{
  "employee": 1,            
  "date": "2025-05-26",     
  "status": "Present"      
}

-----------------------------------------------------## Setup Instructions-------------------------------------------------------

1. Clone the repo:

```bash
git clone using my repo
cd employee-project


