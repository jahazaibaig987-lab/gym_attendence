import pandas as pd
from pathlib import Path
import joblib

# Load model
model_path = Path(__file__).parent.parent / "artifacts/gym_attendance_model.pkl"
model = joblib.load(model_path)

def predict_attendance(new_data):
    """
    new_data: dictionary with same columns as training features
    Example:
    new_data = {
        "member_id": 101,
        "visit_date": "2026-03-08",
        "age": 25,
        "duration": 60,
        "calories_burned": 300,
        "check_in_time": 18,  # convert time to number
        ...
    }
    """
    df = pd.DataFrame([new_data])
    prediction = model.predict(df)
    return prediction[0]

if __name__ == "__main__":
    sample = {
        "member_id": 101,
        "visit_date": 0,  # convert date numeric if needed
        "age": 25,
        "duration": 60,
        "calories_burned": 300,
        "check_in_time": 18,
        "some_other_col": 0  # replace as per your CSV
    }
    result = predict_attendance(sample)
    print("Predicted Attendance:", result)
    
    
