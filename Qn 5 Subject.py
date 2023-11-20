import numpy as np

# Assuming you have a 4x4 matrix
student_scores = np.array([
    [80, 75, 90, 85],
    [92, 88, 78, 95],
    [87, 84, 89, 80],
    [78, 90, 92, 88]
])

# Calculate the average score for each subject (column-wise mean)
subject_averages = np.mean(student_scores, axis=0)

# Determine the subject with the highest average score
highest_avg_subject = np.argmax(subject_averages)

# Print the results
print("Average scores for each subject:", subject_averages)
print("Subject with the highest average score:", highest_avg_subject)
