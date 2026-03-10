import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# cleaned data path
DATA_PATH = Path(__file__).parent.parent / "data/cleaned_gym_workout.csv"

def train_model():

    # load data
    df = pd.read_csv(DATA_PATH)

    # features and target
    X = df.drop("attendance_status", axis=1)
    y = df["attendance_status"]

    # train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # model training
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42
    )
    model.fit(X_train, y_train)
    # prediction
    y_pred = model.predict(X_test)

    # evaluation
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # save model
    model_path = Path(__file__).parent.parent / "artifacts/gym_attendance_model.pkl"
    joblib.dump(model, model_path)

    print("Model saved successfully!")

if __name__ == "__main__":
    train_model()