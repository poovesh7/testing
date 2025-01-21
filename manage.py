# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'postscribers.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()



#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
"""
import os
import sys



def main():
    """Run administrative tasks."""
    # Set default settings module for the Django application
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'postscribers.settings')
    try:
        # Import Django's execute_from_command_line utility
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Pass command-line arguments to Django's execute_from_command_line function
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
