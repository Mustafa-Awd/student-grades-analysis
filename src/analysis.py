from pathlib import Path
import pandas as pd
from rich import print
from rich.console import Console
from rich.table import Table

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "students.csv"

data = pd.read_csv(DATA_PATH)
console = Console()

def load_data():
    console.rule("Mission 1")
    print("[green]======================== Top 5 ========================[/green]\n")
    print(data.iloc[0:5, :], "\n")
    print("[green]======================== Bottom 5 ========================[/green]\n")
    print(data.tail())

    return data


def inspect_data():
    console.rule("Mission 2")
    student_count = len(data)
    column_count = len(data.columns)

    print(f"\n[bold cyan]There are {student_count} students/rows and {column_count} columns.[/bold cyan] [red]No null values[/red]\n")
    print(f"[green]column names[/green]: {list(data.columns)}")
    print(f"[green]column types[/green]: {data.dtypes.astype(str).to_list()}\n")


def basic_statistics():
    console.rule("Mission 3")

    # filter subjects to include only numerical columns excluding age
    subjects = data.select_dtypes(include="number").columns.to_list()[1:]
    # Loop through subjects and print average max and min
    for subject in subjects:
        print(f"[bold green]{subject}[bold green]")
        print(f'[blue] Average mark: {data[subject].mean():.2f}, Highest mark: {data[subject].max()}, Lowest mark: {data[subject].min()}[blue]')
    return

def simple_table_creator(data:pd.DataFrame, subject, table_title):
    table = Table(title=table_title)

    table.add_column("Name")
    table.add_column("City")
    table.add_column(subject, justify="right")

    for _, student in data.iterrows():
        table.add_row(
            student["Name"],
            student["City"],
            str(student[subject])
        )

    return table

def student_queries():
    console.rule("Mission 4")

    top_math_student = data.loc[data["Math"].idxmax()]
    bottom_english_student = data.loc[data["English"].idxmin()]
    top_chemistry_students = data.loc[data["Chemistry"] > 90]
    bottom_math_students = data.loc[data["Math"] < 70]

    chemistry_table = simple_table_creator(top_chemistry_students, "Chemistry", "Top chemistry students")
    math_table = simple_table_creator(bottom_math_students, "Chemistry", "Bottom chemistry students")

    print(f'Top math student: {top_math_student["Name"]}')
    print(f'Bottom english student: {bottom_english_student["Name"]}\n')
    console.print(chemistry_table)
    console.print(math_table)