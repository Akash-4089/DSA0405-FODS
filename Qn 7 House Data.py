import numpy as np

# Example data (replace this with your actual data)
# Assume the columns are in order: bedrooms, square footage, sale price
house_data = np.array([
    [3, 1500, 250000],
    [4, 1800, 300000],
    [5, 2000, 350000],
    [4, 1600, 280000],
    [3, 1400, 230000],
    [5, 2200, 380000],
])

# Extract the relevant columns (bedrooms and sale price)
bedrooms = house_data[:, 0]  # Assuming bedrooms is the first column (index 0)
sale_price = house_data[:, 2]  # Assuming sale price is the third column (index 2)

# Find indices of houses with more than four bedrooms
indices_more_than_four_bedrooms = np.where(bedrooms > 4)

# Extract sale prices of houses with more than four bedrooms
sale_price_more_than_four_bedrooms = sale_price[indices_more_than_four_bedrooms]

# Calculate the average sale price
average_sale_price_more_than_four_bedrooms = np.mean(sale_price_more_than_four_bedrooms)

# Print the result
print("Average sale price of houses with more than four bedrooms:", average_sale_price_more_than_four_bedrooms)
