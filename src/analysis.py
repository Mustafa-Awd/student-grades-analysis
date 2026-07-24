from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "students.csv"


def load_data():
    data = pd.read_csv(DATA_PATH)
    print("======== Top 5 ============\n")
    print(data.iloc[0:5, :])
    print("======== Bottom 5 ============\n")
    print(data.tail())