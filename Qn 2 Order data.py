import pandas as pd

# Sample data creation (replace this with your actual dataset)
data = {
    'customer_id': [1, 2, 1, 3, 2, 3],
    'order_date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06'],
    'product_name': ['A', 'B', 'A', 'C', 'B', 'C'],
    'order_quantity': [3, 5, 2, 1, 4, 2]
}

order_data = pd.DataFrame(data)

# 1. Total number of orders made by each customer
total_orders_by_customer = order_data['customer_id'].value_counts()
print("Total number of orders by each customer:")
print(total_orders_by_customer)
print("\n")

# 2. Average order quantity for each product
average_order_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()
print("Average order quantity for each product:")
print(average_order_quantity_per_product)
print("\n")

# 3. Earliest and latest order dates
order_data['order_date'] = pd.to_datetime(order_data['order_date'])  # Convert to datetime
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()

print(f"Earliest Order Date: {earliest_order_date}")
print(f"Latest Order Date: {latest_order_date}")