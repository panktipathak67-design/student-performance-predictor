🎓 Student Performance Predictor

A beginner-friendly Machine Learning project built with Python that predicts a student's final marks based on study hours, attendance, assignment completion, and previous exam marks.

📌 Project Overview
The Student Performance Predictor uses Linear Regression to estimate a student's final examination marks.

The model considers the following factors:
- 📚 Study Hours
- 📅 Attendance Percentage
- 📝 Assignment Completion
- 📊 Previous Exam Marks

Based on these inputs, the program predicts the student's expected final marks and classifies their performance.

🤖 Machine Learning Algorithm

Linear Regression
Linear Regression is used to find the relationship between the input features and the student's final marks.

🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn
- Linear Regression

📂 Project Structure

student-performance-predictor/
│
├── student_predictor.py<br>
├── requirements.txt<br>
└── README.md<br>

⚙️ Installation

Install the required Python libraries:
pip install -r requirements.txt

Or install them individually:
pip install pandas scikit-learn

▶️ How to Run

Run the Python program using:
python student_predictor.py

Enter the required information when prompted:
Study hours per day
Attendance percentage
Assignment completion percentage
Previous exam marks

The program will then display:
- Predicted final marks
- Performance category

📊 Example

----- STUDENT PERFORMANCE PREDICTOR -----
Study hours per day: 6<br>
Attendance percentage: 85<br>
Assignment completion percentage: 80<br>
Previous exam marks: 72<br>
Predicted Final Marks: 76.XX<br>
Performance: Very Good<br>

📈 Model Evaluation

The model is evaluated using:
- Mean Absolute Error (MAE)
- R² Score

These metrics help measure how accurately the model predicts student performance.

🎯 Performance Categories

Marks| Performance
90+| Excellent
75–89| Very Good
60–74| Good
40–59| Average
Below 40| Needs Improvement

💡 Learning Outcomes

Through this project, I learned:
- How to create a dataset using Pandas
- How to separate features and target variables
- How to split data into training and testing sets
- How to train a Linear Regression model
- How to make predictions
- How to evaluate a Machine Learning model
- How to use Git and GitHub for project management

🚀 Future Improvements

Future versions of this project can include:
- Larger real-world student datasets
- Multiple Machine Learning algorithms
- Data visualization
- Graphical User Interface (GUI)
- Streamlit web application
- Model comparison
- Improved prediction accuracy
