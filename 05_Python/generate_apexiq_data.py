import pandas as pd
from faker import Faker
import random
import os
from datetime import datetime, timedelta

# -----------------------------
# ApexIQ Enterprise Generator
# -----------------------------

fake = Faker("en_IN")
Faker.seed(42)
random.seed(42)

# Create dataset folder
os.makedirs("03_Datasets", exist_ok=True)

print("=" * 60)
print("      ApexIQ Enterprise Data Generator v1.0")
print("=" * 60)

def random_date(start_year=2023, end_year=2025):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 6, 30)
    return start + timedelta(
        days=random.randint(0, (end - start).days)
    )

# ------------------------------------
# Generate Customers
# ------------------------------------

customers = []

segments = ["Premium", "Gold", "Silver"]

for i in range(1, 10001):

    customers.append({

        "customer_id": i,
        "customer_code": f"CUS{i:05}",
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "gender": random.choice(["Male", "Female"]),
        "email": fake.unique.email(),
        "phone": fake.msisdn()[:10],
        "city": fake.city(),
        "state": fake.state(),
        "country": "India",
        "customer_segment": random.choice(segments),
        "registration_date": random_date().date(),
        "loyalty_points": random.randint(100, 5000)

    })

customer_df = pd.DataFrame(customers)

customer_df.to_csv(
    "03_Datasets/customers.csv",
    index=False
)

print("✅ Customers Generated :", len(customer_df))

# ------------------------------------
# Generate Employees
# ------------------------------------

employees = []

departments = [
    "Sales",
    "Finance",
    "Human Resources",
    "Operations",
    "Inventory",
    "Customer Success",
    "Executive"
]

designations = [
    "Executive",
    "Senior Executive",
    "Analyst",
    "Manager",
    "Team Lead",
    "Assistant Manager"
]

for i in range(1, 2001):

    employees.append({

        "employee_id": i,
        "employee_code": f"EMP{i:05}",
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "gender": random.choice(["Male","Female"]),
        "department": random.choice(departments),
        "designation": random.choice(designations),
        "salary": random.randint(30000,180000),
        "joining_date": random_date(2018,2025).date(),
        "performance_rating": round(random.uniform(3.0,5.0),1),
        "employment_status":"Active"

    })

employee_df = pd.DataFrame(employees)

employee_df.to_csv(
    "03_Datasets/employees.csv",
    index=False
)

print("✅ Employees Generated :", len(employee_df))

# ------------------------------------
# Generate Products
# ------------------------------------

products = []

categories = [
    "Electronics",
    "Laptops",
    "Mobiles",
    "Home Appliances",
    "Furniture",
    "Fashion",
    "Sports",
    "Books"
]

brands = [
    "Dell","HP","Apple","Samsung","Sony",
    "LG","Nike","Adidas","Godrej","Lenovo",
    "Asus","Acer","Boat","JBL","Puma"
]

for i in range(1,1001):

    cost = random.randint(500,50000)
    price = int(cost * random.uniform(1.15,1.60))

    products.append({

        "product_id": i,
        "product_code": f"PRD{i:05}",
        "product_name": fake.word().title() + " Product",
        "category": random.choice(categories),
        "brand": random.choice(brands),
        "cost_price": cost,
        "selling_price": price,
        "stock_quantity": random.randint(10,500),
        "reorder_level": random.randint(10,50),
        "status": "Active"

    })

product_df = pd.DataFrame(products)

product_df.to_csv(
    "03_Datasets/products.csv",
    index=False
)

print("✅ Products Generated :", len(product_df))

# ------------------------------------
# Generate Orders
# ------------------------------------

orders = []

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash"
]

status = [
    "Delivered",
    "Pending",
    "Cancelled"
]

for i in range(1,50001):

    customer = random.randint(1,10000)
    employee = random.randint(1,2000)
    warehouse = random.randint(1,5)

    total = random.randint(500,80000)

    discount = round(total*random.uniform(0,0.15),2)

    taxable = total-discount

    tax = round(taxable*0.18,2)

    final = round(taxable+tax,2)

    orders.append({

        "order_id":i,
        "order_number":f"ORD{i:06}",
        "customer_id":customer,
        "employee_id":employee,
        "warehouse_id":warehouse,
        "order_date":random_date().date(),
        "order_status":random.choice(status),
        "payment_method":random.choice(payment_methods),
        "total_amount":total,
        "discount":discount,
        "tax":tax,
        "final_amount":final

    })

order_df=pd.DataFrame(orders)

order_df.to_csv(
    "03_Datasets/orders.csv",
    index=False
)

print("✅ Orders Generated :",len(order_df))

# ------------------------------------
# Generate Order Items
# ------------------------------------

order_items = []
order_item_id = 1

for order_id in range(1, 50001):

    # each order will have 1 to 4 products
    num_items = random.randint(1, 4)

    selected_products = random.sample(range(1, 1001), num_items)

    for product_id in selected_products:

        product_row = product_df.loc[product_df["product_id"] == product_id].iloc[0]

        quantity = random.randint(1, 5)
        unit_price = product_row["selling_price"]
        discount = round(unit_price * quantity * random.uniform(0, 0.10), 2)
        total_price = round((unit_price * quantity) - discount, 2)

        order_items.append({
            "order_item_id": order_item_id,
            "order_id": order_id,
            "product_id": product_id,
            "quantity": quantity,
            "unit_price": unit_price,
            "discount": discount,
            "total_price": total_price
        })

        order_item_id += 1

order_items_df = pd.DataFrame(order_items)

order_items_df.to_csv(
    "03_Datasets/order_items.csv",
    index=False
)

print("✅ Order Items Generated :", len(order_items_df))

# ------------------------------------
# Generate Payments
# ------------------------------------

payments = []

statuses = ["Completed", "Pending", "Refunded"]

for i in range(1, 50001):

    order = order_df.iloc[i - 1]

    payments.append({

        "payment_id": i,
        "payment_code": f"PAY{i:06}",
        "order_id": order["order_id"],
        "payment_date": order["order_date"],
        "payment_method": order["payment_method"],
        "payment_status": random.choice(statuses),
        "transaction_amount": order["final_amount"],
        "transaction_reference": f"TXN{100000+i}"

    })

payment_df = pd.DataFrame(payments)

payment_df.to_csv(
    "03_Datasets/payments.csv",
    index=False
)

print("✅ Payments Generated :", len(payment_df))