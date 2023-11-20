import numpy as np

# Example data (replace this with your actual data)
# Assuming the second column (index 1) contains product prices
sales_data = np.array([
    ["Product A", 20.0],
    ["Product B", 30.0],
    ["Product C", 25.0],
    ["Product D", 40.0],
])

# Extract the product prices
product_prices = sales_data[:, 1]  # Assuming product prices are in the second column

# Convert prices to float if needed
product_prices = product_prices.astype(float)

# Calculate the average price
average_price = np.mean(product_prices)

# Print the result
print("Average price of all products sold in the past month:", average_price)
