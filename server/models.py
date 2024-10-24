from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
import re
from config import db

# Models go here!
metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)

class Customer(db.Model, SerializerMixin):
    __tablename__ = "customers"

    serialize_rules = ('-orders.customer',)

    id = db.Column(db.Integer, primary_key=True)
    cust_name = db.Column(db.String, unique = True, nullable = False)
    contact = db.Column(db.String)
    #address = db.Column(db.String, nullable = False)
    email = db.Column(db.String, unique = True, nullable = False)
    phone = db.Column(db.String, nullable = True)
    #cust_discount = db.Column(db.Integer)

    # one to many relationship with order
    orders = db.relationship('Order', back_populates='customer')

    @validates('email')
    def validate_email(self, key, email):
        # validates email entry format
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format")
        return email

    def __repr__(self):
        return f"<Customer {self.id}, {self.cust_name}, {self.email}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'cust_name': self.cust_name,
            'contact': self.contact,
            'email': self.email,
            'phone' : self.phone
        }

class Product(db.Model, SerializerMixin):
    __tablename__ = "products"

    serialize_rules = ('-order_products.product', '-returns.product')

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = True)
    price = db.Column(db.Float, nullable = False)
    stock_qty = db.Column(db.Integer, nullable = False)
    in_stock = db.Column(db.Boolean, default = True)

    # many to many relationship with order through OrderProducts
    order_products = db.relationship('OrderProducts', back_populates = 'product')
    returns = db.relationship('Returns', back_populates = 'product')

    orders= association_proxy('order_products', 'order')

    @validates('price')
    def validate_price(self, key, price):
        #validates if price is positive
        if price < 0:
            raise ValueError("Price must be a positive value")
        return price

    def __repr__(self):
        return f"<Product {self.id}, {self.product_name}, {self.price}, in_stock={self.in_stock}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'product_name': self.product_name,
            'description': self.description,
            'price': self.price,
            'stock_qty' : self.stock_qty,
            'in_stock' : self.in_stock
        }

class Order(db.Model, SerializerMixin):
    __tablename__ = "orders"

    serialize_rules = ('-customer.orders', '-order_products.order', '-returns.order')

    id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable = False)
    order_date = db.Column(db.DateTime, nullable = False)
    total_amount = db.Column(db.Float, nullable = False)
    status = db.Column(db.String, default='pending')

    # one to many relationship with return
    returns = db.relationship('Returns', back_populates = 'order')
    # many to many relationship with product through OrderProducts
    order_products = db.relationship('OrderProducts', back_populates = 'order', cascade ='all, delete-orphan')
    # back reference to customer
    customer = db.relationship('Customer', back_populates='orders')

    products = association_proxy('order_products', 'product')

    def __repr__(self):
        return f"<Order {self.id}, {self.customer_id}, {self.order_date}, {self.total_amount}, {self.status}>"

    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'order_date': self.order_date.isoformat(),
            'total_amount': self.total_amount,
            'status': self.status
        }
    
class Returns(db.Model, SerializerMixin):
    __tablename__ = "returns"

    serialize_rules = ('-order.returns','-product.returns')

    id = db.Column(db.Integer, primary_key = True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable = False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable = False)
    return_date = db.Column(db.DateTime, nullable = False)
    reason = db.Column(db.String, nullable = True)
    status = db.Column(db.String, default='requested')

    # back reference to Order and Product
    order = db.relationship('Order', back_populates='returns')
    product = db.relationship('Product')

    def __repr__(self):
        return f"<Returns {self.id}, {self.order_id}, {self.product_id}, status={self.status}>"

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'return_date': self.return_date.isoformat(),
            'reason': self.reason,
            'status': self.status
        }
    
class OrderProducts(db.Model, SerializerMixin):
    __tablename__ = "order_products"
    __table_args__ = (db.UniqueConstraint('order_id', 'product_id'),)

    serialize_rules = ('-order.order_products', '-product.order_products')

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable = False)

    # one to one relationship between order and product
    order = db.relationship('Order', back_populates = 'order_products')
    product = db.relationship('Product', back_populates = 'order_products')

    def __repr__(self):
        return f"<OrderProducts {self.id}, order_id={self.order_id}, product_id={self.product_id}, quantity={self.quantity}>"

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'quantity': self.quantity
        }