<img width="2950" height="1647" alt="Screenshot 2025-11-27 222917" src="https://github.com/user-attachments/assets/4dce1c06-32cc-4b86-9968-789e30c89d40" />


Loan Approval Prediction Web App
💳 Loan Approval Prediction Web App

A machine learning–powered Flask application that predicts Loan Approval Status and provides a Risk Score based on user-entered financial and demographic details.

This project uses two ML models:

Classification model → Predicts whether the loan will be approved

Regression model → Predicts a Risk Score

🚀 Features

✔ Web interface built with HTML + CSS (Dark Mode 4-column UI)
✔ Flask backend with POST form handling
✔ Uses two models:

final_model.pkl (Classification)

regressor_model.pkl (Regression Risk Score)

✔ Converts education level to numeric values
✔ Real-time prediction results
✔ Clean UI with scrollable inputs

🗂 Project Structure
├── app.py
├── final_model.pkl
├── regressor_model.pkl
├── templates/
│   └── index2.html
├── static/
│   └── (optional CSS if used)
└── README.md

🛠 Technologies Used

Python

Flask

Pandas

Pickle

HTML/CSS

Machine Learning Models (Classification + Regression)

⚙️ How It Works
1️⃣ User enters the following data:

Age

Annual Income

Credit Score

Education Level

Experience

Loan Amount

Loan Duration

Monthly Debt

Bankruptcy History

Default History

Credit History Length

Total Assets

Monthly Income

Net Worth

Interest Rates

Monthly Loan Payment

Debt-to-Income Ratio

2️⃣ Flask processes the data and maps:
EducationLevel = {
    "High School": 0,
    "Associate": 1,
    "Bachelor": 2,
    "Master": 3,
    "Doctorate": 4
}

3️⃣ Data is sent into:

Classification model → Predicts Loan Approved / Not Approved

Regression model → Predicts Risk Score

4️⃣ Output is displayed on the UI:
Predicted Loan Status: Loan Approved  
RiskScore: (value)

▶️ How to Run Locally
1. Clone the repository:
git clone https://github.com/yourusername/loan-approval-prediction.git
cd loan-approval-prediction

2. Install dependencies:
pip install flask pandas pickle5

3. Run the Flask app:
python app.py

4. Open the app in your browser:
http://127.0.0.1:5000/

🧠 Model Files

Place these trained models in the project root:

final_model.pkl → Binary classification (Approve/Not Approve)

regressor_model.pkl → Risk Score regression

Both are loaded in app.py:

model = pickle.load(open("final_model.pkl", "rb"))
model_1 = pickle.load(open("regressor_model.pkl", "rb"))

🎨 User Interface

The UI contains:

A 4-column structured form

Dark mode theme

Scrollable container

Clean & modern design

Created in:

templates/index2.html

📬 Output Example
Predicted Loan Status: Loan Approved
RiskScore: 72.693

🤝 Contributing

Feel free to submit issues or pull requests to improve:

UI

ML model

Code optimization

Documentation
