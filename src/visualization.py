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

    # Histogram for average marks done by ChatGPT
    plt.hist(data["Average"], bins=10, color="blue", edgecolor="black", alpha=0.7)
    plt.title("Distribution of Student Averages")
    plt.xlabel("Average Mark")
    plt.ylabel("Number of Students")
    plt.xlim(0, 100)
    plt.xticks(range(0, 101, 10))
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(6,6))

    # Pie chart for grade distribution done by ChatGPT
    plt.pie(
        grade_counts,
        labels=grade_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Grade Distribution")
    plt.axis("equal")
    plt.tight_layout()

    plt.show()

create_visualizations()