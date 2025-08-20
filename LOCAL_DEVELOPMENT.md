# 🏠 Local Development Guide

This guide will walk you through setting up and running your Saleor-based online store locally for development and testing.

## 📋 Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.8+** (Python 3.11 recommended)
- **PostgreSQL** database server
- **Redis** server (optional for local testing)
- **Git** (for version control)

## 🚀 Quick Start (Recommended)

The easiest way to get started is using our automated setup script:

```bash
# Run the automated setup script
python run_local.py
```

This script will:
- ✅ Install all Python dependencies
- ✅ Create environment configuration
- ✅ Set up the database
- ✅ Create sample products
- ✅ Start the development server

## 🛠️ Manual Setup

If you prefer to set up everything manually, follow these steps:

### 1. Install Python Dependencies

```bash
# Install local development requirements
pip install -r requirements-local.txt
```

### 2. Set Up Environment Variables

Create a `.env.local` file in your project root:

```bash
# Copy the example file
cp env.local.example .env.local

# Edit the file with your local database credentials
nano .env.local  # or use your preferred editor
```

**Important**: Update the database credentials in `.env.local` to match your local PostgreSQL setup.

### 3. Set Up PostgreSQL Database

```bash
# Connect to PostgreSQL
psql -U postgres

# Create the database
CREATE DATABASE saleor_local;

# Create a user (optional, you can use postgres user)
CREATE USER saleor_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE saleor_local TO saleor_user;

# Exit PostgreSQL
\q
```

### 4. Run Database Migrations

```bash
# Run migrations to create database tables
python manage_local.py migrate
```

### 5. Create Admin User

```bash
# Create a superuser for admin access
python manage_local.py createsuperuser
```

### 6. Load Sample Data

```bash
# Run the sample data script
python manage_local.py shell
```

In the Django shell:
```python
from store.models import Product

# Create sample products
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
    }
]

for product_data in products:
    Product.objects.create(**product_data)

print(f"Created {len(products)} sample products!")
exit()
```

### 7. Start the Development Server

```bash
# Start Django development server
python manage_local.py runserver
```

## 🌐 Access Your Local Store

Once the server is running, you can access:

- **Store Homepage**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **API Endpoint**: http://127.0.0.1:8000/api/products/

## 🎨 Frontend Development

For the React frontend, open a new terminal and navigate to the frontend directory:

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will be available at: http://localhost:3000/

## 🔧 Development Workflow

### Adding New Products

1. **Via Admin Panel** (Recommended for testing):
   - Go to http://127.0.0.1:8000/admin/
   - Login with your superuser credentials
   - Click on "Products" → "Add Product"
   - Fill in the product details and save

2. **Via Django Shell**:
   ```bash
   python manage_local.py shell
   ```
   ```python
   from store.models import Product
   Product.objects.create(
       name='New Product',
       description='Product description',
       price=99.99,
       image='https://via.placeholder.com/300x300'
   )
   ```

### Modifying the Store

- **Templates**: Edit files in `templates/store/`
- **Views**: Modify `store/views.py`
- **Models**: Update `store/models.py`
- **URLs**: Edit `store/urls.py`

### Database Changes

When you modify models:

```bash
# Create new migrations
python manage_local.py makemigrations

# Apply migrations
python manage_local.py migrate
```

## 🧪 Testing Features

### Test the Store

1. **View Products**: Visit the homepage to see your products
2. **Admin Panel**: Add/edit products through the admin interface
3. **API Testing**: Test the API endpoint at `/api/products/`

### Test the Frontend

1. **Product Display**: Check if products load correctly
2. **Responsive Design**: Test on different screen sizes
3. **Navigation**: Test all links and buttons

## 🐛 Troubleshooting

### Common Issues

#### Database Connection Error
```
django.db.utils.OperationalError: could not connect to server
```
**Solution**: 
- Ensure PostgreSQL is running
- Check database credentials in `.env.local`
- Verify database exists

#### Port Already in Use
```
Error: That port is already in use
```
**Solution**:
- Kill the process using the port: `lsof -ti:8000 | xargs kill -9`
- Or use a different port: `python manage_local.py runserver 8001`

#### Module Not Found
```
ModuleNotFoundError: No module named 'store'
```
**Solution**:
- Ensure you're in the project root directory
- Check that all `__init__.py` files exist
- Verify the project structure

#### Static Files Not Loading
**Solution**:
- Run: `python manage_local.py collectstatic`
- Check `STATIC_URL` and `STATIC_ROOT` in settings

### Getting Help

- Check Django error logs in the terminal
- Verify all dependencies are installed
- Ensure database is accessible
- Check file permissions

## 📁 Project Structure

```
OnlineStore/
├── local_store/           # Local Django project
│   ├── settings.py        # Local development settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI application
├── store/                 # Store app
│   ├── models.py         # Product models
│   ├── views.py          # Store views
│   ├── urls.py           # Store URLs
│   └── admin.py          # Admin configuration
├── templates/             # HTML templates
│   └── store/            # Store templates
├── frontend/              # React frontend
├── requirements-local.txt # Local Python dependencies
├── manage_local.py        # Local Django management
├── run_local.py          # Automated setup script
└── .env.local            # Local environment variables
```

## 🚀 Next Steps

Once your local development environment is working:

1. **Customize the Store**: Modify templates, add new features
2. **Test Functionality**: Ensure everything works as expected
3. **Prepare for Production**: Update settings for Render deployment
4. **Deploy**: Follow the Render deployment guide

## 💡 Tips

- **Keep `.env.local` in `.gitignore`** to avoid committing sensitive data
- **Use the automated script** (`run_local.py`) for quick setup
- **Test frequently** as you make changes
- **Backup your database** before major changes
- **Use Django Debug Toolbar** for development insights

---

**Happy coding! 🎉**

