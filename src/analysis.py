from pathlib import Path
import pandas as pd
from rich import print
from rich.console import Console

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