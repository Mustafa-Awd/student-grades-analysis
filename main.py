from src.analysis import load_data, inspect_data, basic_statistics, student_queries
def main():
    print("Hello from student-grades-analysis!")

    load_data()
    inspect_data()
    basic_statistics()
    student_queries()


if __name__ == "__main__":
    main()
