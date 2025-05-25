#!/usr/bin/env python
"""
This is the entry-point script for all Django command-line utilities.
When you run `python manage.py`, this is the file that gets executed.
"""

import os
import sys

def main():
    """Run administrative tasks like runserver, migrate, createsuperuser, etc."""
    
    # Set the default settings module for the 'django' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_project.settings')

    try:
        # Import the function to execute command-line utilities.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise a helpful error if Django is not installed or not available
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Call the command-line utility (e.g. runserver, migrate, etc.)
    execute_from_command_line(sys.argv)

# This ensures the main() function runs only when the script is executed directly
if __name__ == '__main__':
    main()
