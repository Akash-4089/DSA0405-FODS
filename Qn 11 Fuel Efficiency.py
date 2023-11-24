import numpy as np

# Create a NumPy array with fuel efficiency data (miles per gallon)
fuel_efficiency = np.array([25, 30, 22])  # Replace with your actual data

# Calculate the average fuel efficiency
average_fuel_efficiency = np.mean(fuel_efficiency)

print("Average Fuel Efficiency:", average_fuel_efficiency, "miles per gallon")

# Determine percentage improvement between two car models
index_model_A = 0  # Replace with the actual index of Model A
index_model_B = 1  # Replace with the actual index of Model B

fuel_efficiency_model_A = fuel_efficiency[index_model_A]
fuel_efficiency_model_B = fuel_efficiency[index_model_B]

percentage_improvement = ((fuel_efficiency_model_B - fuel_efficiency_model_A) / fuel_efficiency_model_A) * 100

print(f"Percentage Improvement from Model A to Model B: {percentage_improvement:.2f}%")
