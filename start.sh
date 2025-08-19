#!/usr/bin/env bash
# Start script for Saleor on Render

echo "Starting Saleor..."

# Set environment variables if not already set
export PYTHONPATH="${PYTHONPATH}:${PWD}"

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the application
gunicorn saleor.wsgi:application --bind 0.0.0.0:$PORT --workers 4 --timeout 120
