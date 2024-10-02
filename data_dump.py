import os
import sys
import django
from django.conf import settings
from django.core.management import call_command

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'signage.settings')
django.setup()

def dump_data():
    try:
        print("Dumping data from SQLite...")
        from django.db import connections
        
        with open('data.json', 'w', encoding='utf-8') as f:
            call_command('dumpdata', '--exclude', 'auth.permission', '--exclude', 'contenttypes', stdout=f)
        print("Data successfully dumped to data.json")
        connections.close_all()  # Close any lingering connections
        print("Connections closed.")
    except Exception as e:
        print(f"Error dumping data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Check the flag from settings
        # Step 1: Dump data from SQLite (if exists)
        dump_data()
        print("Process complete!")
