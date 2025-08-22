import urllib
from sqlalchemy import create_engine
import pandas as pd
import random
import numpy as np
from faker import Faker
# Define products and statuses


fake = Faker()
random.seed(42)
np.random.seed(42)

# Generate unique customers
num_customers = 300
customer_data = []

for customer_id in range(1000, 1000 + num_customers):
    name = fake.name() if random.random() > 0.025 else ""  # 2% missing names
    customer_data.append([customer_id, name])

df_customers = pd.DataFrame(customer_data, columns=["Customer_ID", "Name"])
# df_customers.to_csv("customers.csv", index=False)

products = ['Red T-Shirt', 'Blue Jeans', 'Black Hat', 'White Sneakers', 'Green Hoodie']
statuses = ['Delivered', 'Returned', 'Processing', 'Cancelled']
product_prices = {
    'Red T-Shirt': 20,
    'Blue Jeans': 35,
    'Black Hat': 15,
    'White Sneakers': 50,
    'Green Hoodie': 40
}

# Generate messy transactions
num_sales = 1200
sales_data = []

for trans_id in range(1, num_sales + 1):
    transaction_id = f"T{str(trans_id).zfill(5)}"
    customer_id = random.randint(1000, 1000 + num_customers - 1)
    product = random.choice(products)

    # Messy product name
    messy_product = product.lower() if random.random() < 0.3 else product.upper() if random.random() < 0.3 else product
    messy_product = f" {messy_product} " if random.random() < 0.2 else messy_product

    # Messy date
    date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%B %d, %Y", "%Y/%m/%d"]
    purchase_date = fake.date_between(start_date='-1y', end_date='today')
    date_format = random.choice(date_formats)
    date_str = purchase_date.strftime(date_format)

    quantity = random.choice([1, 2, 3, None]) if random.random() < 0.95 else None
    price = product_prices[product] if random.random() > 0.05 else None
    total = (price * quantity) if price and quantity else None

    status = random.choice(statuses)
    status = status.lower() if random.random() < 0.3 else status.upper() if random.random() < 0.3 else status

    sales_data.append([
        transaction_id,
        customer_id,
        messy_product,
        date_str,
        quantity,
        price,
        total,
        status
    ])

df_transactions = pd.DataFrame(sales_data, columns=[
    "Transaction_ID", "Customer_ID", "Product", "Purchase_Date", "Quantity", "Price", "Total", "Status"
])
# df_transactions.to_csv("transactions.csv", index=False)


server = '.\SQLEXPRESS'
database = 'Storedb'
params = urllib.parse.quote_plus(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'
)
# Creating sqlalchemy engine
engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')
df_customers.to_sql('Customer', con=engine, if_exists='replace', index=False)
df_transactions.to_sql('Transactions', con= engine, if_exists='replace', index=False)
print("Data inserted into SQL Server successfully!")
