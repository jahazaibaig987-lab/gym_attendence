from pathlib import Path
import pandas as pd

# Updated CSV file name
DATA_PATH = Path(__file__).parent.parent / "data/gym_workout.csv"

def load_data():
    # CSV load karo
    df = pd.read_csv(DATA_PATH)
    print("Data loaded successfully!")
    print(df.head())  # Top 5 rows check karo
    return df

if __name__ == "__main__":
    load_data()