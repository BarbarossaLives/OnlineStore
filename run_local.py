#!/usr/bin/env python
"""
Local development setup and run script.
"""
import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n[INFO] {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"[SUCCESS] {description} completed successfully!")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {description} failed!")
        print(f"Error: {e.stderr}")
        return False

def setup_environment():
    """Set up the local development environment."""
    print("[INFO] Setting up local development environment...")
    
    # Create .env.local file if it doesn't exist
    env_file = '.env.local'
    if not os.path.exists(env_file):
        print(f"[INFO] Creating {env_file} file...")
        with open(env_file, 'w', encoding='utf-8') as f:
            f.write("""# Local Development Environment Variables
DEBUG=True
SECRET_KEY=django-insecure-local-development-key-change-this
ALLOWED_HOSTS=localhost,127.0.0.1

# Note: Using SQLite for local development (no database setup required)
# PostgreSQL will be used in production on Render

# Email Configuration (Console for development)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
""")
        print(f"[SUCCESS] {env_file} created successfully!")
    
    # Install Python dependencies
    if not run_command("pip install -r requirements-local.txt", "Installing Python dependencies"):
        return False
    
    # Create necessary directories
    os.makedirs('static', exist_ok=True)
    os.makedirs('media', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    
    print("[SUCCESS] Environment setup completed!")
    return True

def run_migrations():
    """Run Django migrations."""
    return run_command("python manage_local.py migrate", "Running database migrations")

def create_superuser():
    """Create a superuser if none exists."""
    print("\n[INFO] Checking if superuser exists...")
    try:
        result = subprocess.run(
            "python manage_local.py shell -c \"from django.contrib.auth.models import User; print('Superuser exists' if User.objects.filter(is_superuser=True).exists() else 'No superuser found')\"",
            shell=True, capture_output=True, text=True
        )
        if "No superuser found" in result.stdout:
            print("[INFO] Creating superuser...")
            print("Please enter the following details:")
            run_command("python manage_local.py createsuperuser", "Creating superuser")
        else:
            print("[SUCCESS] Superuser already exists!")
    except:
        print("[WARNING] Could not check superuser status. You can create one manually later.")

def load_sample_data():
    """Load sample products for testing."""
    print("\n[INFO] Loading sample products...")
    sample_data_script = """
from store.models import Product

# Create sample products if none exist
if Product.objects.count() == 0:
    products = [
        {
            'name': 'Sample Product 1',
            'description': 'This is a sample product description for testing purposes.',
            'price': 29.99,
            'image': 'https://via.placeholder.com/300x300'
        },
        {
            'name': 'Sample Product 2',
            'description': 'Another sample product to test the store functionality.',
            'price': 49.99,
            'image': 'https://via.placeholder.com/300x300'
        },
        {
            'name': 'Sample Product 3',
            'description': 'A third sample product to demonstrate the grid layout.',
            'price': 79.99,
            'image': 'https://via.placeholder.com/300x300'
        }
    ]
    
    for product_data in products:
        Product.objects.create(**product_data)
    
    print(f"Created {len(products)} sample products!")
else:
    print(f"{Product.objects.count()} products already exist!")
"""
    
    with open('temp_sample_data.py', 'w', encoding='utf-8') as f:
        f.write(sample_data_script)
    
    run_command("python temp_sample_data.py", "Loading sample data")
    os.remove('temp_sample_data.py')

def start_server():
    """Start the Django development server."""
    print("\n[INFO] Starting Django development server...")
    print("Server will be available at: http://127.0.0.1:8000/")
    print("Admin panel: http://127.0.0.1:8000/admin/")
    print("API endpoint: http://127.0.0.1:8000/api/products/")
    print("\nPress Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        subprocess.run("python manage_local.py runserver", shell=True)
    except KeyboardInterrupt:
        print("\n\nServer stopped. Goodbye!")

def main():
    """Main function to set up and run the local development environment."""
    print("Local Store Development Setup")
    print("=" * 40)
    print("Using SQLite for local development (no PostgreSQL required)")
    print("=" * 40)
    
    # Check if Python is available
    if not run_command("python --version", "Checking Python installation"):
        print("[ERROR] Python is not available. Please install Python 3.8+ and try again.")
        return
    
    # Setup environment
    if not setup_environment():
        print("[ERROR] Environment setup failed. Please check the errors above.")
        return
    
    # Run migrations
    if not run_migrations():
        print("[ERROR] Database setup failed. Please check the errors above.")
        return
    
    # Create superuser
    create_superuser()
    
    # Load sample data
    load_sample_data()
    
    # Start server
    start_server()

if __name__ == "__main__":
    main()

