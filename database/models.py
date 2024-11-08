# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 08, 2024 15:35:05
# Database: sqlite:////tmp/tmp.Az5C6ayao7/Home_Hardware/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Category(SAFRSBaseX, Base):
    """
    description: Represents product categories, such as tools or paint.
    """
    __tablename__ = 'category'
    _s_collection_name = 'Category'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductList : Mapped[List["Product"]] = relationship(back_populates="category")



class Customer(SAFRSBaseX, Base):
    """
    description: Represents customers of the hardware store.
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    registration_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")



class Employee(SAFRSBaseX, Base):
    """
    description: Represents employees working in the hardware store.
    """
    __tablename__ = 'employee'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String)
    salary = Column(Float, nullable=False)
    hire_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    DepartmentList : Mapped[List["Department"]] = relationship(back_populates="manager")
    EmployeeDepartmentList : Mapped[List["EmployeeDepartment"]] = relationship(back_populates="employee")



class Supplier(SAFRSBaseX, Base):
    """
    description: Represents suppliers who provide products to the hardware store.
    """
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_name = Column(String)
    contact_email = Column(String)
    phone = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductList : Mapped[List["Product"]] = relationship(back_populates="supplier")



class Department(SAFRSBaseX, Base):
    """
    description: Represents different departments within the hardware store.
    """
    __tablename__ = 'department'
    _s_collection_name = 'Department'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    manager_id = Column(ForeignKey('employee.id'))

    # parent relationships (access parent)
    manager : Mapped["Employee"] = relationship(back_populates=("DepartmentList"))

    # child relationships (access children)
    EmployeeDepartmentList : Mapped[List["EmployeeDepartment"]] = relationship(back_populates="department")



class Order(SAFRSBaseX, Base):
    """
    description: Represents customer orders placed with the hardware store.
    """
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'), nullable=False)
    order_date = Column(DateTime)
    total_amount = Column(Float)
    shipped = Column(Boolean)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="order")



class Product(SAFRSBaseX, Base):
    """
    description: Represents products available in the hardware store.
    """
    __tablename__ = 'product'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    category_id = Column(ForeignKey('category.id'))
    supplier_id = Column(ForeignKey('supplier.id'))

    # parent relationships (access parent)
    category : Mapped["Category"] = relationship(back_populates=("ProductList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("ProductList"))

    # child relationships (access children)
    DiscountList : Mapped[List["Discount"]] = relationship(back_populates="product")
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="product")
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="product")



class Discount(SAFRSBaseX, Base):
    """
    description: Represents discounts available on products.
    """
    __tablename__ = 'discount'
    _s_collection_name = 'Discount'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'), nullable=False)
    discount_percentage = Column(Float, nullable=False)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("DiscountList"))

    # child relationships (access children)



class EmployeeDepartment(SAFRSBaseX, Base):
    """
    description: Represents the relationship between employees and departments.
    """
    __tablename__ = 'employee_department'
    _s_collection_name = 'EmployeeDepartment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    employee_id = Column(ForeignKey('employee.id'), nullable=False)
    department_id = Column(ForeignKey('department.id'), nullable=False)
    start_date = Column(DateTime)

    # parent relationships (access parent)
    department : Mapped["Department"] = relationship(back_populates=("EmployeeDepartmentList"))
    employee : Mapped["Employee"] = relationship(back_populates=("EmployeeDepartmentList"))

    # child relationships (access children)



class Inventory(SAFRSBaseX, Base):
    """
    description: Represents inventory records with product quantities.
    """
    __tablename__ = 'inventory'
    _s_collection_name = 'Inventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'), nullable=False)
    available_quantity = Column(Integer, nullable=False)
    last_updated = Column(DateTime)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("InventoryList"))

    # child relationships (access children)



class OrderItem(SAFRSBaseX, Base):
    """
    description: Represents items in a customer order.
    """
    __tablename__ = 'order_item'
    _s_collection_name = 'OrderItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'), nullable=False)
    product_id = Column(ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderItemList"))
    product : Mapped["Product"] = relationship(back_populates=("OrderItemList"))

    # child relationships (access children)
    ReturnList : Mapped[List["Return"]] = relationship(back_populates="order_item")



class Return(SAFRSBaseX, Base):
    """
    description: Represents product returns from customers.
    """
    __tablename__ = 'return'
    _s_collection_name = 'Return'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_item_id = Column(ForeignKey('order_item.id'), nullable=False)
    return_date = Column(DateTime)
    refund_amount = Column(Float, nullable=False)

    # parent relationships (access parent)
    order_item : Mapped["OrderItem"] = relationship(back_populates=("ReturnList"))

    # child relationships (access children)
