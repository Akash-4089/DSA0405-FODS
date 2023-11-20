import numpy as np

# Example data (replace these with your actual data)
time_intervals = np.array([0, 1, 2, 3, 4])  # Time intervals in seconds
vertical_positions = np.array([0, 10, 24, 36, 40])  # Vertical positions in meters

# Calculate the change in vertical position
delta_vertical_position = np.diff(vertical_positions)

# Calculate the change in time
delta_time = np.diff(time_intervals)

# Calculate the average velocity
average_velocity = delta_vertical_position / delta_time

# Print the results
print("Time Intervals:", time_intervals)
print("Vertical Positions:", vertical_positions)
print("Change in Vertical Position:", delta_vertical_position)
print("Change in Time:", delta_time)
print("Average Velocity:", average_velocity)
