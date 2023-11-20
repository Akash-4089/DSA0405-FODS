import matplotlib.pyplot as plt

# Example data (replace this with your actual data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales_values = [10000, 12000, 15000, 11000, 13000]

# Create a line plot
plt.plot(months, sales_values, marker='o', linestyle='-', color='b', label='Monthly Sales')

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.title('Monthly Sales Data')
plt.legend()  # Add legend if multiple lines

# Show the plot
plt.show()

# Create a bar plot
plt.bar(months, sales_values, color='c', label='Monthly Sales')

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.title('Monthly Sales Data')
plt.legend()  # Add legend if multiple bars

# Show the plot
plt.show()
