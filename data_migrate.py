   # Step 2: Migrate schema to PostgreSQL
import os
import sys
import django
from django.conf import settings
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'signage.settings')
django.setup()

def load_data():
    try:
        print("Loading data into PostgreSQL...")
        call_command('loaddata', 'data.json')
        print("Data successfully loaded into PostgreSQL")
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1) 

if __name__ == "__main__":
    
        
        try:
            print("Migrating schema to PostgreSQL...")
            call_command('migrate')
            print("Schema successfully migrated")
        except Exception as e:
            print(f"Error during migration: {e}")
            sys.exit(1)

        # Step 3: Load data into PostgreSQL
        print(settings.FLAG)
        load_data()
        print("Process complete!")
    
         