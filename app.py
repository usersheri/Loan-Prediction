from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model and scaler
model = pickle.load(open("final_model.pkl", "rb"))
model_1 = pickle.load(open("regressor_model.pkl", "rb"))
@app.route('/')
def home():
    return render_template('index2.html', prediction_text='')
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the input values from the form
    Age = int(request.form['Age'])
    AnnualIncome = float(request.form['AnnualIncome'])
    CreditScore = int(request.form['CreditScore'])
    EducationLevel =(request.form['EducationLevel'])
    Experience = int(request.form['Experience'])
    LoanAmount = float(request.form['LoanAmount'])
    LoanDuration = int(request.form['LoanDuration'])
    MonthlyDebtPayments = float(request.form['MonthlyDebtPayments'])
    BankruptcyHistory = float(request.form['BankruptcyHistory'])
    PreviousLoanDefaults = float(request.form['PreviousLoanDefaults'])
    LengthOfCreditHistory = int(request.form['LengthOfCreditHistory'])
    TotalAssets = float(request.form['TotalAssets'])
    MonthlyIncome = float(request.form['MonthlyIncome'])
    NetWorth = float(request.form['NetWorth'])
    BaseInterestRate = float(request.form['BaseInterestRate'])
    InterestRate = float(request.form['InterestRate'])
    MonthlyLoanPayment = float(request.form['MonthlyLoanPayment'])
    TotalDebtToIncomeRatio = float(request.form['TotalDebtToIncomeRatio'])
    # Prepare the input data for prediction
    input_data = pd.DataFrame([[Age, AnnualIncome, CreditScore, EducationLevel, 
    Experience,
       LoanAmount, LoanDuration, MonthlyDebtPayments,
       BankruptcyHistory, PreviousLoanDefaults, LengthOfCreditHistory,
       TotalAssets, MonthlyIncome, NetWorth, BaseInterestRate,
       InterestRate, MonthlyLoanPayment, TotalDebtToIncomeRatio]],
       columns=['Age', 'AnnualIncome', 'CreditScore', 'EducationLevel','Experience','LoanAmount','LoanDuration','MonthlyDebtPayments','BankruptcyHistory','PreviousLoanDefaults','LengthOfCreditHistory','TotalAssets',
                'MonthlyIncome','NetWorth','BaseInterestRate','InterestRate','MonthlyLoanPayment','TotalDebtToIncomeRatio'])
    input_data['EducationLevel']=input_data['EducationLevel'].map({'High School':0,'Associate':1,'Bachelor':2,'Master':3,'Doctorate':4})
    # Make the prediction
    prediction = model.predict(input_data)
    Risk_score = model_1.predict(input_data)
    if prediction == 0:
        Loan_Approval_status = "Loan not Approved"
    elif prediction == 1:
        Loan_Approval_status = "Loan Approved"
    else:
        Loan_Approval_status = "invalid"

    # prediction_text = f" Predicted Loan Status: {Loan_Approval_status} \n RiskScore: {Risk_score[0]}"
    return render_template('index2.html',
              loan_status=Loan_Approval_status,
                    risk_score=Risk_score[0]
)

if __name__ == "__main__":
    app.run(debug=True)
