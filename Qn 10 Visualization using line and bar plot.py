import matplotlib.pyplot as plt

# Example data (replace this with your actual data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature_values = [15, 18, 22, 25, 30, 32, 35, 33, 28, 23, 19, 16]

# Create a line plot for temperature
plt.plot(months, temperature_values, marker='o', linestyle='-', color='r', label='Monthly Temperature')

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature Data')
plt.legend()

# Show the plot
plt.show()


# Example data (replace this with your actual data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall_values = [50, 45, 60, 30, 20, 10, 5, 15, 25, 40, 55, 50]

# Create a scatter plot for rainfall
plt.scatter(months, rainfall_values, color='b', label='Monthly Rainfall')

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall Data')
plt.legend()

# Show the plot
plt.show()
