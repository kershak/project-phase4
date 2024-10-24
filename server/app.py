#!/usr/bin/env python3

from flask import request, Flask, jsonify, make_response
from flask_restful import Resource, Api
from flask_migrate import Migrate

# Local imports
from config import app, db, api
from models import db, Customer, Product, Order, Returns, OrderProducts
from flask_cors import CORS
import os
# Add your model imports
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'instance/app.db')}")

app = Flask(__name__)

CORS(app) 

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)
# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

# @app.route('/customers', methods = ['GET'])
# def manage_customers():
#     if request.method == 'GET':
#         customers = Customer.query.all()
#         return jsonify([{'id': customers.id, 'name': customers.cust_name, 'email': customers.email}])

class CustomerInfo(Resource):
    def get(self):
        customers = Customer.query.all()
        return make_response(jsonify([customer.to_dict() for customer in customers]), 200)
        #return make_response(jsonify([{'id': cust.id, 'name': cust.cust_name, 'email': cust.email  } for cust in customers]), 200)
    
    def post(self):
        data = request.get_json()
        new_customer = Customer(cust_name=data['cust_name'], email = data['email'], phone = data.get('phone'))
        db.session.add(new_customer)
        db.session.commit()
        #return make_response(jsonify({'id': new_customer.id, 'name': new_customer.cust_name}), 201)
        return make_response(jsonify(new_customer.to_dict()), 201)

class CustomerById(Resource):
    def get(self, customer_id):
        customer = Customer.query.filter(Customer.id == customer_id).first()
        if not customer:
            return make_response(jsonify({"error": "Customer not found"}), 404)
        #return make_response(jsonify({'id': customer.id, 'name': customer.cust_name, 'email': customer.email}), 200)
        return make_response(jsonify([customer.to_dict()]), 200)
    
    def delete(self, customer_id):
        customer = Customer.query.filter(Customer.id == customer_id).first()
        if not customer:
            return make_response(jsonify({"error": "Customer not found"}), 404)
        db.session.delete(customer)
        db.session.commit()
        return make_response(jsonify({'message': 'Customer deleted'}), 204)
    
class ProductInfo(Resource):
    def get(self):
        products = Product.query.all()
        #return make_response(jsonify([{'id': prod.id, 'name': prod.product_name, 'description': prod.description } for prod in products]), 200)
        return make_response(jsonify([prod.to_dict() for prod in products]), 200)

    def post(self):
        data = request.get_json()
        new_product = Product(
            product_name=data['product_name'],
            description = data['description'],
            price= data['price'],
            stock_qty = data['stock_qty'],
            in_stock = data.get('in_stock', True)
        )
        db.session.add(new_product)
        db.session.commit()
        #return make_response(jsonify({'id': new_product.id, 'product_name': new_product.product_name}), 201)
        return make_response(jsonify(new_product.to_dict()), 201)


class ProductById(Resource):
    def get(self, product_id):
        product = Product.query.filter(Product.id == product_id).first()
        if not product:
            return make_response(jsonify({"error": "Prodcut not found"}), 404)
        #return make_response(jsonify({'id': product.id, 'product_name': product.product_name, 'description': product.description}), 200)
        return make_response(jsonify([product.to_dict()]), 200)

    def delete(self,product_id):
        product = Product.query.filter(Product.id == product_id).first()
        if not product:
            return make_response(jsonify({"error": "Product not found"}), 404)
        db.session.delete(product)
        db.session.commit()
        return make_response(jsonify({'message': 'Product deleted'}), 204)

class OrderInfo(Resource):
    def get(self):
        orders = Order.query.all()
        #return make_response(jsonify([{'id': ord.id, 'customer_id': ord.customer_id, 'total_amount': ord.total_amount, 'status': ord.status} for ord in orders]),200)
        return make_response(jsonify([ord.to_dict() for ord in orders]), 200)
    
    def post(self):
        data = request.get_json()
        if not isinstance(data, list) or len(data) !=1:
            return make_response(jsonify({'error': 'Invalid input format'}), 400)
        order_data = data[0]
        new_order = Order(
            customer_id=order_data['customer_id'],
            order_date=order_data['order_date'],
            total_amount=order_data['total_amount'],
            status=order_data.get('status', 'pending')
        )
        db.session.add(new_order)
        db.session.commit()
        #return make_response(jsonify({'id': new_order.id, 'customer_id': new_order.customer_id,'total_amount': new_order.total_amount}), 201)
        return make_response(jsonify(new_order.to_dict()), 201)
    
class OrderById(Resource):
    def get(self, order_id):
        order = Order.query.filter(Order.id == order_id).first()
        if not order:
            return make_response(jsonify({"error": "Order not found"}), 404)
        #return make_response(jsonify({'id': order.id, 'customer_id': order.customer_id, 'total_amount': order.total_amount}),200)
        return make_response(jsonify([order.to_dict()]), 200)

    def delete(self,order_id):
        order = Order.query.filter(Order.id == order_id).first()
        if not order:
            return make_response(jsonify({"error": "Order not found"}), 404)
        for order_product in order.order_products:
            db.session.delete(order_product)
        db.session.delete(order)
        db.session.commit()
        return make_response(jsonify({'message': 'Order deleted'}), 204)

class ReturnInfo(Resource):
    def get(self):
        returns = Returns.query.all()
        #return make_response(jsonify([{'id': retu.id, 'order_id': retu.order_id, 'product_id': retu.product_id, 'return_date': retu.return_date, 'status':retu.status} for retu in returns]), 200)
        return make_response(jsonify([retu.to_dict() for retu in returns]), 200)
    
    def post(sefl):
        data = request.get_json()
        new_return = Returns(
            order_id=data['order_id'],
            product_id=data['product_id'],
            return_date=data.get('return_date'),
            reason=data.get('reason', ''),
            status=data.get('status', 'requested')
        )
        db.session.add(new_return)
        db.session.commit()
        return make_response(jsonify({'id': new_return.id, 'order_id': new_return.order_id}), 201)

class ReturnById(Resource):
    def get(self, return_id):
        return_entry = Returns.query.filter(Returns.id == return_id).first()
        if not return_entry:
            return make_response(jsonify({"error": "Return entry not found"}), 404)
        #return make_response(jsonify({'id': return_entry.id, 'order_id': return_entry.order_id, 'product_id': return_entry.product_id, 'status': return_entry.status}), 200)
        return make_response(jsonify([return_entry.to_dict()]), 200)

    def delete(self,return_id):
        return_entry = Returns.query.filter(Returns.id == return_id).first()
        if not return_entry:
            return make_response(jsonify({"error": "Return entry not found"}), 404)
        db.session.delete(return_entry)
        db.session.commit()
        return make_response(jsonify({'message': 'Return deleted'}), 204)
    
api.add_resource(CustomerInfo, '/customers', endpoint = 'customers')
api.add_resource(CustomerById, '/customers/<int:customer_id>', endpoint = 'customer_by_id')
api.add_resource(ProductInfo, '/products', endpoint = 'products')
api.add_resource(ProductById, '/products/<int:product_id>', endpoint = 'product_by_id')
api.add_resource(OrderInfo, '/orders', endpoint = 'orders')
api.add_resource(OrderById, '/orders/<int:order_id>', endpoint = 'orders_by_id')
api.add_resource(ReturnInfo, '/returns', endpoint = 'returns')
api.add_resource(ReturnById, '/returns/<int:return_id>', endpoint = 'returns_by_id')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

