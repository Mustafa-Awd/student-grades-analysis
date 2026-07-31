from src.analysis import load_data, inspect_data, basic_statistics, student_queries, create_new_columns
def main():
    print("Hello from student-grades-analysis!")

    load_data()
    inspect_data()
    basic_statistics()
    student_queries()
    create_new_columns()

if __name__ == "__main__":
    main()
