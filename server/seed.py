from datetime import datetime
from app import app
from models import db, Customer, Product, Order, Returns, OrderProducts

# Seed data
def seed_data():
    # Create Customers
    customer1 = Customer(cust_name="John Doe", contact="123 Main St", email="john@example.com", phone="555-1234")
    customer2 = Customer(cust_name="Jane Smith", contact="456 Oak St", email="jane@example.com", phone="555-5678")
    
    # Create Products
    product1 = Product(product_name="Laptop", description="A high-performance laptop", price=1200.50, stock_qty=50)
    product2 = Product(product_name="Smartphone", description="A new smartphone with 5G", price=800.75, stock_qty=100)
    
    # Create Orders
    order1 = Order(customer=customer1, order_date=datetime.now(), total_amount=1200.50, status='completed')
    order2 = Order(customer=customer2, order_date=datetime.now(), total_amount=1601.50, status='pending')
    
    # Create OrderProducts
    order_product1 = OrderProducts(order=order1, product=product1, quantity=1)
    order_product2 = OrderProducts(order=order2, product=product1, quantity=1)
    order_product3 = OrderProducts(order=order2, product=product2, quantity=1)
    
    # Create Returns
    return1 = Returns(order=order1, product=product1, return_date=datetime.now(), reason="Defective item", status="processed")
    
    # Add all the data to the session
    db.session.add_all([customer1, customer2, product1, product2, order1, order2, order_product1, order_product2, order_product3, return1])
    
    # Commit the session to the database
    db.session.commit()

# Run the seeding function when the file is executed
if __name__ == '__main__':
    with app.app_context():
        # Create the tables if they don't exist
        db.create_all()
        # Seed the data
        seed_data()
        print("Database seeded successfully!")




# #!/usr/bin/env python3

# # Standard library imports
# from random import randint, choice as rc
# from datetime import datetime, timedelta
# import pandas as pd
# import os

# # Remote library imports
# from faker import Faker

# # Local imports
# from app import app
# from models import db, Customer,Product,Order,Returns,OrderProducts


# fake = Faker()

# def seed_customers(num_customers=10):
#         """Seed the database with random customer data."""
#         with app.app_context():
#             print("Seeding customers...")
#             for _ in range(num_customers):
#                 cust_name = fake.company()
#                 contact = fake.name()
#                 email = fake.email()
#                 phone = fake.phone_number()
                
#                 new_customer = Customer(
#                     name=cust_name,
#                     contact = contact,
#                     email=email,
#                     phone=phone
#                 )
#                 db.session.add(new_customer)
            
#             db.session.commit()
#             print(f"{num_customers} customers added to the database.")

# def seed_products_from_excel(file_path):
#         """Seed the database with product data from an Excel file."""
#         with app.app_context():
#             print("Seeding products from Excel file...")
#             df = pd.read_excel(file_path)
#             # if 'product_name' not in df.Columns:
#             #      raise KeyError("The 'product_name' column is missing from the excel file.")

#             for index, row in df.iterrows():
#                 new_product = Product(
#                     #name=row['name'],
#                     description=row.get('description', ''),
#                     price=row['price'],
#                     stock_quantity=row['stock_quantity'],
#                     in_stock=row.get('in_stock', True)
#                 )
#                 db.session.add(new_product)

#             db.session.commit()
#             print(f"{len(df)} products added to the database.")

# if __name__ == '__main__':
#     BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#     DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'instance/app.db')}")
#     with app.app_context():
#         db.create_all() 
#     excel_file_path = os.path.join(BASE_DIR,'productlist.xlsx')
#     seed_products_from_excel(excel_file_path)



    # with app.app_context():
    #     print("Starting seed...")
    #     # Seed code goes here!

    #     db.drop_all()
    #     db.create_all()

    #     #seed customers
    #     customers = []
    #     for _ in range(20):
    #         customer = Customer(
    #             cust_name = fake.unique.company(),
    #             contact = fake.name(),
    #             email = fake.unique.email(),
    #             phone = fake.unique.phone_number()
    #         )
    #         customers.append(customer)
    #     db.session.bulk_save_objects(customers)
    #     db.session.commit()
    #     print(f"Seeded {len(customers)} customers.")

        #seed products
        # products = []
        # for _ in range(20):
        #     product = Product(
        #         product_name = fake.word().capitalize(),
        #         description = fake.sentence(),
        #         price=round(randint(10, 100) + randint(0, 99) / 100, 2),
        #         stock_quantity=randint(0, 50),
        #         in_stock=randint(0, 1) == 1
        #     )
        #     products.append(product)
        # db.session.bulk_save_objects(product)
        # db.session.commit()
        # print(f"Seeded {len(product)} products.")

        #seed orders
        # orders = []
        # for _ in range(15):  # Create 15 orders
        #     order = Order(
        #         customer_id=rc(customers).id,
        #         order_date=fake.date_time_this_year(),
        #         total_amount=round(randint(20, 500) + randint(0, 99) / 100, 2),
        #         status=rc(['pending', 'shipped', 'delivered'])
        #     )
        #     orders.append(order)
        # db.session.bulk_save_objects(orders)
        # db.session.commit()
        # print(f"Seeded {len(orders)} orders.")

        # # Seed returns
        # returns = []
        # for _ in range(5):  # Create 5 returns
        #     return_entry = Returns(
        #         order_id=rc(orders).id,
        #         #product_id=rc(products).id,
        #         return_date=fake.date_time_this_year(),
        #         reason=fake.sentence(),
        #         status=rc(['requested', 'approved', 'denied'])
        #     )
        #     returns.append(return_entry)
        # db.session.bulk_save_objects(returns)
        # db.session.commit()
        # print(f"Seeded {len(returns)} returns.")

        # Seed order_products
        # order_products = []
        # for order in orders:
        #     num_products = randint(1, 5)  # Each order has 1 to 5 products
        #     chosen_products = rc(products, k=num_products)
        #     for product in chosen_products:
        #         order_product = OrderProducts(
        #             order_id=order.id,
        #             product_id=product.id,
        #             quantity=randint(1, 3)  # Quantity between 1 and 3
        #         )
        #         order_products.append(order_product)
        # db.session.bulk_save_objects(order_products)
        # db.session.commit()
        # print(f"Seeded {len(order_products)} order products.")

#print("Seeding completed!")
