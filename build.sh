#!/usr/bin/env bash
# Build script for Render deployment

echo "Starting Saleor build process..."

# Install system dependencies
apt-get update
apt-get install -y postgresql-client

# Install Python dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p media static

echo "Build completed successfully!"
