import pandas as pd
from pathlib import Path
from data_ingestion import load_data

def process_data():
    # Step 1: Load data
    df = load_data()
    
     
    
    # Step 2: Missing values check
    print("Missing values before fill:")
    print(df.isnull().sum())
    
    # Step 3: Fill missing values
    # Numeric columns -> fill with median
    num_cols = df.select_dtypes(include='number').columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    
    # Categorical columns -> fill with mode
    cat_cols = df.select_dtypes(include='object').columns
    df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])
    
    # Step 4: Categorical to numeric conversion
    for col in cat_cols:
        df[col] = df[col].astype('category').cat.codes
    
    print("Data processed successfully!")
    print(df.head())  # Top 5 rows
    
    # Optional: save cleaned data
    cleaned_path = Path(__file__).parent.parent / "artifacts/cleaned_gym_workout.csv"
    df.to_csv(cleaned_path, index=False)
    print(f"Cleaned data saved at {cleaned_path}")
    
    return df

if __name__ == "__main__":
    process_data()

