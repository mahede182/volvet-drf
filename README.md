# Volvet E-commerce API

![License](https://img.shields.io/badge/license-MIT-blue.svg)

Volvet is a modern e-commerce API built with Django and Django REST Framework, providing a robust backend for online shopping platforms.

## Features

- **User Authentication**: JWT-based authentication system
- **Product Management**: CRUD operations for products and categories
- **Shopping Cart**: Add, remove, and manage cart items
- **Order Processing**: Create and track orders
- **Admin Panel**: Full-featured Django admin interface
- **API Documentation**: Swagger and Redoc support

## Technologies Used

- Django 4.2
- Django REST Framework
- SimpleJWT for authentication
- PostgreSQL (recommended)
- Redis (for caching, optional)
- Celery (for background tasks, optional)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/volvet-drf.git
   cd volvet-drf
   ```

2. Create and activate virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory with the following content:

   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_URL=postgres://user:password@localhost:5432/volvet
   ```

5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Create superuser:

   ```bash
   python manage.py createsuperuser
   ```

7. Run development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication

- `POST /api/v1/auth/users/login/` - User login
- `POST /api/v1/auth/users/register/` - User registration

### Products

- `GET /api/v1/products/` - List all products
- `GET /api/v1/products/{slug}/` - Get product details
- `GET /api/v1/products/categories/` - List all categories

### Cart

- `GET /api/v1/cart/` - Get user's cart
- `POST /api/v1/cart/add_item/` - Add item to cart
- `POST /api/v1/cart/remove_item/` - Remove item from cart

### Orders

- `GET /api/v1/orders/` - List user's orders
- `POST /api/v1/orders/` - Create new order

## API Documentation

Explore the API using Swagger or Redoc:

- Swagger UI: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- Redoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

## Environment Variables

| Variable         | Description                   | Default Value |
| ---------------- | ----------------------------- | ------------- |
| `SECRET_KEY`     | Django secret key             | -             |
| `DEBUG`          | Debug mode                    | False         |
| `DATABASE_URL`   | Database connection URL       | -             |
| `EMAIL_HOST`     | Email host for sending emails | -             |
| `EMAIL_PORT`     | Email port                    | -             |
| `EMAIL_USER`     | Email username                | -             |
| `EMAIL_PASSWORD` | Email password                | -             |

## Running Tests

To run the test suite:
