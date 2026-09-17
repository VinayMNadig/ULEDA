from app.database.session import SessionLocal
from app.database.models import (
    Customer,
    Employee,
    Product,
    Supplier,
    Order,
    Payment,
)

db = SessionLocal()

# -------------------------
# Customers
# -------------------------
customers = [
    Customer(first_name="Rahul", last_name="Sharma", email="rahul@gmail.com", phone="9876543210", city="Bangalore"),
    Customer(first_name="Anjali", last_name="Patil", email="anjali@gmail.com", phone="9876543211", city="Mysore"),
    Customer(first_name="Kiran", last_name="Rao", email="kiran@gmail.com", phone="9876543212", city="Hubli"),
    Customer(first_name="Sneha", last_name="Reddy", email="sneha@gmail.com", phone="9876543213", city="Mangalore"),
    Customer(first_name="Arjun", last_name="Nair", email="arjun@gmail.com", phone="9876543214", city="Bangalore"),
]

db.add_all(customers)

# -------------------------
# Employees
# -------------------------
employees = [
    Employee(name="Ramesh", department="Sales", salary=50000, hire_date="2024-01-10"),
    Employee(name="Suresh", department="HR", salary=45000, hire_date="2023-06-15"),
    Employee(name="Priya", department="IT", salary=70000, hire_date="2022-11-01"),
]

db.add_all(employees)

# -------------------------
# Products
# -------------------------
products = [
    Product(product_name="Laptop", category="Electronics", price=65000, stock=20),
    Product(product_name="Keyboard", category="Electronics", price=1200, stock=100),
    Product(product_name="Mouse", category="Electronics", price=800, stock=150),
]

db.add_all(products)

# -------------------------
# Suppliers
# -------------------------
suppliers = [
    Supplier(supplier_name="ABC Traders", contact="9876500000", city="Bangalore"),
    Supplier(supplier_name="XYZ Pvt Ltd", contact="9876500001", city="Chennai"),
]

db.add_all(suppliers)

db.commit()

print("Customers Added")
print("Employees Added")
print("Products Added")
print("Suppliers Added")