import pandas as pd
import numpy as np

np.random.seed(42)
num_properties = 1000

data = {
    'Property_ID': range(1, num_properties + 1),
    'Location': np.random.choice(['City', 'Suburb', 'Rural'], num_properties),
    'Bedrooms': np.random.randint(1, 6, num_properties),
    'Area_SqFeet': np.random.randint(1000, 5000, num_properties),
    'Listing_Price': np.random.randint(100000, 500000, num_properties)
}

property_data = pd.DataFrame(data)

# 1. The average listing price of properties in each location
average_listing_price_per_location = property_data.groupby('Location')['Listing_Price'].mean()

# 2. The number of properties with more than four bedrooms
num_properties_more_than_four_bedrooms = len(property_data[property_data['Bedrooms'] > 4])

# 3. The property with the largest area
property_with_largest_area = property_data.loc[property_data['Area_SqFeet'].idxmax()]

# Display the results
print("Average Listing Price of Properties in Each Location:")
print(average_listing_price_per_location)
print("\nNumber of Properties with More than Four Bedrooms:", num_properties_more_than_four_bedrooms)
print("\nProperty with the Largest Area:")
print(property_with_largest_area)