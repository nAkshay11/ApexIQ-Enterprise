import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

HOST = "localhost"
PORT = "5432"
DATABASE = "apexiq_enterprise"
USER = "postgres"
PASSWORD = "Akshay@12345"

password = quote_plus(PASSWORD)

engine = create_engine(
    f"postgresql+psycopg2://{USER}:{password}@{HOST}:{PORT}/{DATABASE}"
)

print("✅ Connected to PostgreSQL")

with engine.begin() as conn:
    conn.execute(text("""
        TRUNCATE TABLE
        finance.payments,
        sales.order_items,
        sales.orders,
        inventory.products,
        common.employees,
        customer.customers
        RESTART IDENTITY CASCADE;
    """))

print("✅ Old data cleared")

# Customers
customers = pd.read_csv("03_Datasets/customers.csv")
customers["customer_status"] = "Active"

customers = customers[
    [
        "customer_id", "customer_code", "first_name", "last_name", "gender",
        "email", "phone", "city", "state", "country", "customer_segment",
        "registration_date", "customer_status", "loyalty_points"
    ]
]

customers.to_sql("customers", engine, schema="customer", if_exists="append", index=False, chunksize=1000)
print(f"✅ Customers Loaded : {len(customers)}")

# Employees
employees = pd.read_csv("03_Datasets/employees.csv")

department_map = {
    "Sales": 1,
    "Finance": 2,
    "Human Resources": 3,
    "Operations": 4,
    "Inventory": 5,
    "Customer Success": 6,
    "Executive": 7
}

employees["department_id"] = employees["department"].map(department_map)
employees["email"] = (
    employees["first_name"].str.lower()
    + "."
    + employees["last_name"].str.lower()
    + employees["employee_id"].astype(str)
    + "@apexiq.com"
)
employees["phone"] = ["9" + str(100000000 + i) for i in range(len(employees))]
employees["manager_name"] = "Not Assigned"

employees = employees[
    [
        "employee_id", "employee_code", "first_name", "last_name", "gender",
        "email", "phone", "department_id", "designation", "manager_name",
        "salary", "joining_date", "employment_status", "performance_rating"
    ]
]

employees.to_sql("employees", engine, schema="common", if_exists="append", index=False, chunksize=1000)
print(f"✅ Employees Loaded : {len(employees)}")

# Products
products = pd.read_csv("03_Datasets/products.csv")

category_map = {
    "Electronics": 1,
    "Laptops": 2,
    "Mobiles": 3,
    "Home Appliances": 4,
    "Furniture": 5,
    "Fashion": 6,
    "Sports": 7,
    "Books": 8
}

products["category_id"] = products["category"].map(category_map)
products["unit_price"] = products["selling_price"]
products["supplier_name"] = "ApexIQ Supplier"
products["product_status"] = products["status"]

products = products[
    [
        "product_id", "product_code", "product_name", "category_id",
        "brand", "unit_price", "cost_price", "stock_quantity",
        "reorder_level", "supplier_name", "product_status"
    ]
]

products.to_sql("products", engine, schema="inventory", if_exists="append", index=False, chunksize=1000)
print(f"✅ Products Loaded : {len(products)}")

# Orders
orders = pd.read_csv("03_Datasets/orders.csv")

orders = orders[
    [
        "order_id", "order_number", "customer_id", "employee_id",
        "warehouse_id", "order_date", "order_status", "payment_method",
        "total_amount", "discount", "tax", "final_amount"
    ]
]

orders.to_sql("orders", engine, schema="sales", if_exists="append", index=False, chunksize=1000)
print(f"✅ Orders Loaded : {len(orders)}")

# Order Items
order_items = pd.read_csv("03_Datasets/order_items.csv")

order_items = order_items[
    [
        "order_item_id", "order_id", "product_id", "quantity",
        "unit_price", "discount", "total_price"
    ]
]

order_items.to_sql("order_items", engine, schema="sales", if_exists="append", index=False, chunksize=1000)
print(f"✅ Order Items Loaded : {len(order_items)}")

# Payments
payments = pd.read_csv("03_Datasets/payments.csv")

payments = payments[
    [
        "payment_id", "payment_code", "order_id", "payment_date",
        "payment_method", "payment_status", "transaction_amount",
        "transaction_reference"
    ]
]

payments.to_sql("payments", engine, schema="finance", if_exists="append", index=False, chunksize=1000)
print(f"✅ Payments Loaded : {len(payments)}")

print("\n🎉 ALL DATA IMPORTED SUCCESSFULLY!")