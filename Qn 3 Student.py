import pandas as pd

# Sample data creation (replace this with your actual dataset)
data = {
    'Student_ID': [1, 2, 3, 4, 5],
    'Course': ['Math', 'English', 'Math', 'Physics', 'English'],
    'Score': [80, 75, 90, 85, 78],
    'Hours_Studied': [10, 8, 12, 15, 9]
}

student_data = pd.DataFrame(data)

# 1. Compute the correlation coefficient between 'Hours_Studied' and 'Score' for each course
correlation_per_course = student_data.groupby('Course')[['Hours_Studied', 'Score']].corr().iloc[0::2, -1]

# 2. Identify courses where the correlation between study hours and scores is the strongest and weakest
strongest_correlation = correlation_per_course.groupby('Course').idxmax().squeeze()
weakest_correlation = correlation_per_course.groupby('Course').idxmin().squeeze()

# 3. Create a new DataFrame that aggregates the average score and average hours studied for each course
average_data = student_data.groupby('Course').agg({'Score': 'mean', 'Hours_Studied': 'mean'}).reset_index()

print("Correlation Coefficient between Hours Studied and Score for Each Course:")
print(correlation_per_course)
print("\nStrongest Correlation per Course:")
print(strongest_correlation)
print("\nWeakest Correlation per Course:")
print(weakest_correlation)
print("\nAverage Score and Average Hours Studied per Course:")
print(average_data)