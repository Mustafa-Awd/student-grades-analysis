from analysis import data, SUBJECTS, create_new_columns
import matplotlib.pyplot as plt

create_new_columns()
grade_counts = data["Grade"].value_counts()


def create_visualizations ():
    print(data.head())
    subject_means = []
    for subject in SUBJECTS:
        subject_mean = data[subject].mean()
        subject_means.append(subject_mean)

    # Bar chart for average marks by subject done by me
    plt.bar(SUBJECTS, subject_means)
    plt.title("Average Marks by Subject")
    plt.ylim(0, 100)
    plt.xlabel("Subjects")
    plt.ylabel("Average Mark")
    plt.show()

    plt.figure(figsize=(8,5))

create_visualizations()