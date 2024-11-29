# Django-OLX-app-RBAC
A fully functional OLX-like platform built using Django and Django REST Framework (DRF). This project allows users to buy and sell products online with role-based access control (RBAC) for Sellers, Customers, and Admins. 


# OLX Clone - Django REST Framework

A fully functional OLX-like platform built using Django and Django REST Framework (DRF). This project allows users to buy and sell products online with role-based access control (RBAC) for **Sellers**, **Customers**, and **Admins**. The project is designed to be scalable, secure, and easy to use.

## Features

### User Management
- **Role-based Access Control**:
  - **Sellers** can create, update, and delete their own products.
  - **Customers** can view and browse available products.
  - **Admins** have full control over all products and users.
- JWT-based authentication for secure API access.
- Restrict product creation to sellers only.

### Product Listings
- **CRUD Operations** for products with the following fields:
  - Seller
  - Title
  - Description
  - Price
  - Status (Available/Sold)
  - Category
  - Location
- Products can be created in bulk or individually by authenticated sellers.
- Prevent sellers from listing duplicate products.
- Restrict sellers from modifying or deleting products belonging to others.

### Order Management
- Customers can place orders for products marked as "available."
- Sellers can manage product availability and mark products as "sold."

### API Documentation
- Integrated Swagger/OpenAPI documentation for easy API testing and exploration.

### Permissions and Security
- Custom permissions to ensure only authorized roles can perform specific actions.
- Validation to prevent duplicate product listings by the same seller.


## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite or PostgreSQL (for the database)
- Django CORS Headers (for cross-origin resource sharing)

## Setting Up the Project

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/bsrashad/Django-OLX-app-RBAC.git
cd myproject

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

python manage.py migrate

### Create a Superuser (for Admin Access)
python manage.py createsuperuser

for running the server:
python manage.py runserver
