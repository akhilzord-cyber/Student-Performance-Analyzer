import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load student data
data = pd.read_csv("data/students.csv")

print("STUDENT PERFORMANCE ANALYZER")
print("=" * 40)

# Show first 5 students
print("\nFirst 5 students:")
print(data.head())

# Subjects
subjects = ["Math", "Physics", "Chemistry", "English", "Computer"]

# Calculate total marks
data["Total"] = data[subjects].sum(axis=1)

# Calculate average marks
data["Average"] = data[subjects].mean(axis=1)

# Calculate grade
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

data["Grade"] = data["Average"].apply(calculate_grade)

# Display student results
print("\nStudent Results:")
print(data[["Student_ID", "Name", "Total", "Average", "Grade"]])

# Top 5 students
print("\nTop 5 Students:")
top_students = data.sort_values("Average", ascending=False).head(5)
print(top_students[["Name", "Average", "Grade"]])

# Average marks for each subject
subject_averages = data[subjects].mean()

print("\nAverage Marks by Subject:")
print(subject_averages)

# Grade distribution
print("\nGrade Distribution:")
print(data["Grade"].value_counts())

# Graph 1: Average marks by subject
subject_averages.plot(kind="bar")

plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()

# Graph 2: Grade distribution
data["Grade"].value_counts().plot(kind="bar")

plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

# Graph 3: Subject correlation
plt.figure(figsize=(10, 6))

sns.heatmap(
    data[subjects].corr(),
    annot=True
)

plt.title("Subject Correlation")
plt.tight_layout()
plt.show()
# ==============================
# FINAL SUMMARY
# ==============================

print("\n" + "=" * 40)
print("FINAL PERFORMANCE SUMMARY")
print("=" * 40)

# Total students
print("Total Students:", len(data))

# Top student
top_student = data.loc[data["Average"].idxmax()]
print("Top Student:", top_student["Name"])
print("Top Student Average:", round(top_student["Average"], 2))

# Best subject
best_subject = subject_averages.idxmax()
print("Best Performing Subject:", best_subject)

# Weakest subject
weakest_subject = subject_averages.idxmin()
print("Weakest Performing Subject:", weakest_subject)

# Overall class average
overall_average = data["Average"].mean()
print("Overall Class Average:", round(overall_average, 2))

# Grade distribution
print("\nGrade Distribution:")
print(data["Grade"].value_counts())

print("=" * 40)
print("ANALYSIS COMPLETED")
print("=" * 40)