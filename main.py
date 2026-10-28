# import numpy & matplotlib libraries 
import numpy as np
import matplotlib.pyplot as plt

# create an array of students, subjects, and grades
students = np.array([
    "Ahmad", "Sara", "Omar", "Lina", "Khaled",
    "Noor", "Yazan", "Maya", "Ali", "Dana"
])

subjects = np.array([
    "English", "Math", "Statistics","Python"
])

grades = np.array([
    [69, 90, 88, 89],
    [95, 92, 94, 90],
    [60, 55, 65, 80],
    [88, 60, 90, 92],
    [72, 88, 74, 80],
    [98, 96, 95, 99],
    [55, 48, 58, 60],
    [82, 88, 85, 90],
    [55, 66, 72, 78],
    [91, 89, 93, 100]
])
print("STUDENT PERFORMANCE ANALYZER")
print("=" * 35)

print("Number of students:", len(students))
print("Number of subjects:", len(subjects))
print("Grades shape:", grades.shape)
print()

# calculate the average grade for each subject
average_subjects = np.mean(grades, axis=0)
for i in range(len(average_subjects)):
    print(f"Average grade for {subjects[i]}: {average_subjects[i]:.2f}")
print()
print(average_subjects)
# calculate the average performance for each student
average_performance = np.mean(grades,axis=1) 
print(average_performance)
print("The best student performance is:",students[np.argmax(average_performance)])
print("The worst student performance is:",students[np.argmin(average_performance)])
print("The best subject performance is:",subjects[np.argmax(average_subjects)])
print("The worst subject performance is:",subjects[np.argmin(average_subjects)])

print("The order of students based on their performance is:",students[np.argsort(average_performance)[::-1]])
print("Students whose average grade is above 90 are:",students[np.where(average_performance > 90)])
print("Students whose average grade is below 60 are:",students[np.where(average_performance < 60)])


# Calculate pass rate for each subject
pass_rate = np.mean(grades >= 60, axis=0) * 100
print(pass_rate)
for i in range(len(subjects)):
    print(f"Pass rate for {subjects[i]}: {pass_rate[i]:.1f}%") 


    
plt.bar(subjects, average_subjects)
plt.title("Average Grades for Each Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Grade")
plt.show()

# Calculate standard deviation for each subject
std_subjects = np.std(grades, axis=0)

for i in range(len(subjects)):
    print(
        f"Standard deviation for {subjects[i]}: "
        f"{std_subjects[i]:.2f}"
    )