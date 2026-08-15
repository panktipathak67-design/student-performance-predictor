# Student Performance Predictor
# ML Algorithm: Linear Regression

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Dataset
data = {
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Attendance": [60, 65, 70, 75, 80, 82, 85, 90, 92, 95],
    "Assignments": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    "Previous_Marks": [45, 50, 55, 60, 65, 68, 72, 78, 82, 88],
    "Final_Marks": [48, 52, 58, 63, 68, 72, 76, 82, 87, 92]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Study_Hours", "Attendance", "Assignments", "Previous_Marks"]]
y = df["Final_Marks"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("----- MODEL PERFORMANCE -----")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R² Score: {r2:.2f}")

# Take input from user
print("\n----- STUDENT PERFORMANCE PREDICTOR -----")

study = float(input("Study hours per day: "))
attendance = float(input("Attendance percentage: "))
assignments = float(input("Assignment completion percentage: "))
previous_marks = float(input("Previous exam marks: "))

# Prediction
student = [[study, attendance, assignments, previous_marks]]
predicted_marks = model.predict(student)[0]

print(f"\nPredicted Final Marks: {predicted_marks:.2f}")

# Performance category
if predicted_marks >= 90:
    performance = "Excellent"
elif predicted_marks >= 75:
    performance = "Very Good"
elif predicted_marks >= 60:
    performance = "Good"
elif predicted_marks >= 40:
    performance = "Average"
else:
    performance = "Needs Improvement"

print(f"Performance: {performance}")
