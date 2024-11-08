# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Connect to the SQLite database
Base = declarative_base()
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')

class Customer(Base):
    """
    description: Represents customers of the hardware store.
    """
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    registration_date = Column(DateTime, default=datetime.datetime.utcnow)

class Supplier(Base):
    """
    description: Represents suppliers who provide products to the hardware store.
    """
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_name = Column(String)
    contact_email = Column(String)
    phone = Column(String)

class Category(Base):
    """
    description: Represents product categories, such as tools or paint.
    """
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)

class Product(Base):
    """
    description: Represents products available in the hardware store.
    """
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False, default=0)
    category_id = Column(Integer, ForeignKey('category.id'))
    supplier_id = Column(Integer, ForeignKey('supplier.id'))

class Order(Base):
    """
    description: Represents customer orders placed with the hardware store.
    """
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    total_amount = Column(Float, default=0.0)
    shipped = Column(Boolean, default=False)

class OrderItem(Base):
    """
    description: Represents items in a customer order.
    """
    __tablename__ = 'order_item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)

class Inventory(Base):
    """
    description: Represents inventory records with product quantities.
    """
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    available_quantity = Column(Integer, nullable=False)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow)

class Employee(Base):
    """
    description: Represents employees working in the hardware store.
    """
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    position = Column(String)
    salary = Column(Float, nullable=False)
    hire_date = Column(DateTime, default=datetime.datetime.utcnow)

class Department(Base):
    """
    description: Represents different departments within the hardware store.
    """
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    manager_id = Column(Integer, ForeignKey('employee.id'))

class EmployeeDepartment(Base):
    """
    description: Represents the relationship between employees and departments.
    """
    __tablename__ = 'employee_department'
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    start_date = Column(DateTime, default=datetime.datetime.utcnow)

class Discount(Base):
    """
    description: Represents discounts available on products.
    """
    __tablename__ = 'discount'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    discount_percentage = Column(Float, nullable=False)

class Return(Base):
    """
    description: Represents product returns from customers.
    """
    __tablename__ = 'return'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_item_id = Column(Integer, ForeignKey('order_item.id'), nullable=False)
    return_date = Column(DateTime, default=datetime.datetime.utcnow)
    refund_amount = Column(Float, nullable=False)

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Add sample data to the tables
customer1 = Customer(name='John Doe', email='john@example.com', phone='555-1234', address='123 Elm St')
supplier1 = Supplier(name='Acme Tools', contact_name='Alice Smith', contact_email='alice@acmetools.com', phone='555-5678')
category1 = Category(name='Hand Tools', description='Manual hand tools such as hammers and screwdrivers.')
product1 = Product(name='Hammer', description='Steel claw hammer', price=9.99, stock_quantity=100, category_id=1, supplier_id=1)
order1 = Order(customer_id=1, order_date=datetime.datetime.utcnow(), total_amount=19.98, shipped=True)
order_item1 = OrderItem(order_id=1, product_id=1, quantity=2, total_price=19.98)
inventory1 = Inventory(product_id=1, available_quantity=98)
employee1 = Employee(name='Jane Doe', position='Sales Associate', salary=30000.0, hire_date=datetime.datetime.utcnow())
department1 = Department(name='Sales', manager_id=1)
employee_department1 = EmployeeDepartment(employee_id=1, department_id=1, start_date=datetime.datetime.utcnow())
discount1 = Discount(product_id=1, discount_percentage=10.0)
return1 = Return(order_item_id=1, return_date=datetime.datetime.utcnow(), refund_amount=9.99)

# Add objects to the session
session.add_all([customer1, supplier1, category1, product1, order1, order_item1, 
                 inventory1, employee1, department1, employee_department1, discount1, return1])

# Commit the session to save the objects to the database
session.commit()

# Close the session
session.close()
