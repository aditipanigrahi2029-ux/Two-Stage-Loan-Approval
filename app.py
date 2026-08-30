# import streamlit as st
# import pandas as pd
# # streamlit run app.py
# from loan import LoanApprovalApp

# st.set_page_config(
#     page_title="Loan Approval Predictor"
# )


# st.title("Loan Approval Prediction")

# st.write(
#     "Enter applicant details to check loan eligibility."
# )

# @st.cache_resource
# def load_model():
#     return LoanApprovalApp()

# model = load_model()

# no_of_dependents = st.number_input(
#     "Number of Dependents",
#     min_value=0
# )

# education = st.selectbox(
#     "Education",
#     ["Graduate", "Not Graduate"]
# )

# self_employed = st.selectbox(
#     "Self Employed",
#     ["Yes", "No"]
# )

# income_annum = st.number_input(
#     "Annual Income",
#     min_value=0.0
# )

# loan_amount = st.number_input(
#     "Loan Amount Requested",
#     min_value=0.0
# )

# loan_term = st.number_input(
#     "Loan Term",
#     min_value=1
# )

# cibil_score = st.number_input(
#     "CIBIL Score"
# )

# residential_assets_value = st.number_input(
#     "Residential Assets Value",
#     min_value=0.0
# )

# commercial_assets_value = st.number_input(
#     "Commercial Assets Value",
#     min_value=0.0
# )

# luxury_assets_value = st.number_input(
#     "Luxury Assets Value",
#     min_value=0.0
# )

# bank_asset_value = st.number_input(
#     "Bank Asset Value",
#     min_value=0.0
# )

# if st.button("Predict"):

#     data = {

#         "no_of_dependents": no_of_dependents,

#         "education": education,

#         "self_employed": self_employed,

#         "income_annum": income_annum,

#         "loan_amount": loan_amount,

#         "loan_term": loan_term,

#         "cibil_score": cibil_score,

#         "residential_assets_value":
#             residential_assets_value,

#         "commercial_assets_value":
#             commercial_assets_value,

#         "luxury_assets_value":
#             luxury_assets_value,

#         "bank_asset_value":
#             bank_asset_value
#     }

#     applicant_df = pd.DataFrame([data])

#     result = model.two_stage_predict(
#         applicant_df
#     )

#     if result["approve"] == 1:

#         st.success(
#             "Loan Approved"
#         )

#         st.metric(
#             "Predicted Loan Amount",
#             f"{result['regression_prediction']:,.2f}"
#         )
#     else:

#         st.error(
#             "Loan Rejected"
#         )





# import streamlit as st
# import requests
# import pandas as pd

# # Page Configuration Setup
# st.set_page_config(page_title="Loan Approval Portal", layout="centered")

# st.title("🏦 Automated Loan Processing Portal")
# st.write("Enter the applicant details below to fire a network request to the FastAPI core engine.")

# # Define the local port address of your running FastAPI server
# API_URL = "http://localhost:8000/predict_loan"


# # User Web Form Elements
# no_of_dependents = st.number_input("Number of Dependents", min_value=0, step=1)
# education = st.selectbox("Education Status", ["Graduate", "Not Graduate"])
# self_employed = st.selectbox("Is Self Employed?", ["Yes", "No"])
# income_annum = st.number_input("Annual Income (₹)", min_value=0.0, step=10000.0)
# loan_amount = st.number_input("Requested Loan Amount (₹)", min_value=0.0, step=50000.0)
# loan_term = st.number_input("Loan Term", min_value=1, step=1)
# cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900, value=750, step=1)
# residential_assets_value = st.number_input("Residential Assets Value (₹)", min_value=0.0)
# commercial_assets_value = st.number_input("Commercial Assets Value (₹)", min_value=0.0)
# luxury_assets_value = st.number_input("Luxury Assets Value (₹)", min_value=0.0)
# bank_asset_value = st.number_input("Bank Asset Value (₹)", min_value=0.0)

# # Submit button logic
# if st.button("Evaluate Application", type="primary"):
    
#     # 1. Package fields into an exact structural dictionary matching the API schema
#     payload = {
#         "no_of_dependents": int(no_of_dependents),
#         "education": education,
#         "self_employed": self_employed,
#         "income_annum": float(income_annum),
#         "loan_amount": float(loan_amount),
#         "loan_term": int(loan_term),
#         "cibil_score": int(cibil_score),
#         "residential_assets_value": float(residential_assets_value),
#         "commercial_assets_value": float(commercial_assets_value),
#         "luxury_assets_value": float(luxury_assets_value),
#         "bank_asset_value": float(bank_asset_value)
#     }
    
#     st.info("Transmitting secure data payload to core API gateway...")
    
#     try:
#         # 2. Fire the network request across your computer's internal ports (REQUESTS POST)
#         response = requests.post(API_URL, json=payload)
        
#         if response.status_code == 200:
#             # Unpack the returned network dictionary JSON response
#             result = response.json()
            
#             # 3. Read the matching backend keys securely ('loan_status')
#             if result.get("loan_status") == 1:
#                 st.success("🎉 Application Accepted: The customer's credit score meets qualification parameters.")
#                 if "regression_prediction" in result:
#                     st.metric(
#                         label="Calculated Approved Loan Allotment Limit",
#                         value=f"₹{result['regression_prediction']:,.2f}"
#                     )
#             else:
#                 st.error("❌ Application Denied: Candidate risk profile fails minimum safety thresholds.")
#         else:
#             st.error(f"Gateway Communication Error! Network Status Code: {response.status_code}")
            
#     except requests.exceptions.ConnectionError:
#         st.error("Fatal Connection Failure: The Streamlit UI cannot reach your FastAPI server! Did you forget to turn on the Uvicorn terminal backend?")















import streamlit as st
import requests
import pandas as pd

# Page Configuration Setup
st.set_page_config(page_title="Loan Approval Portal", layout="centered")

st.title("🏦 Automated Loan Processing Portal")
st.write("Enter the applicant details below to fire a network request to the FastAPI core engine.")

# Define the local port address of your running FastAPI server
API_URL = "http://localhost:8000/predict_loan"

# User Web Form Elements
no_of_dependents = st.number_input("Number of Dependents", min_value=0, step=1)
education = st.selectbox("Education Status", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Is Self Employed?", ["Yes", "No"])
income_annum = st.number_input("Annual Income (₹)", min_value=0.0, step=10000.0)
loan_amount = st.number_input("Requested Loan Amount (₹)", min_value=0.0, step=50000.0)
loan_term = st.number_input("Loan Term", min_value=1, step=1)
cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900, value=750, step=1)
residential_assets_value = st.number_input("Residential Assets Value (₹)", min_value=0.0)
commercial_assets_value = st.number_input("Commercial Assets Value (₹)", min_value=0.0)
luxury_assets_value = st.number_input("Luxury Assets Value (₹)", min_value=0.0)
bank_asset_value = st.number_input("Bank Asset Value (₹)", min_value=0.0)

# Submit button logic
if st.button("Evaluate Application", type="primary"):
    
    # 1. Package fields into an exact structural dictionary matching the API schema
    payload = {
        "no_of_dependents": int(no_of_dependents),
        "education": education,
        "self_employed": self_employed,
        "income_annum": float(income_annum),
        "loan_amount": float(loan_amount),
        "loan_term": int(loan_term),
        "cibil_score": int(cibil_score),
        "residential_assets_value": float(residential_assets_value),
        "commercial_assets_value": float(commercial_assets_value),
        "luxury_assets_value": float(luxury_assets_value),
        "bank_asset_value": float(bank_asset_value)
    }
    
    st.info("Transmitting secure data payload to core API gateway...")
    
    try:
        # 2. Fire the network request across your computer's internal ports
        response = requests.post(API_URL, json=payload)
        print("STREAMLIT SENT:")
        print(payload)

        
        
        if response.status_code == 200:
            result = response.json()
            
            # 3. Read the matching backend keys securely
            if result.get("loan_status") == 1:
                st.success("Application Accepted.")
                if "regression_prediction" in result:
                    st.metric(
                        label="Calculated Approved Loan Allotment Limit",
                        value=f"₹{result['regression_prediction']:,.2f}"
                    )
            else:
                st.error("Sorry Application Denie.")
        else:
            st.error(f"Gateway Communication Error! Network Status Code: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        st.error("Fatal Connection Failure: The Streamlit UI cannot reach your FastAPI server! Did you forget to turn on the Uvicorn terminal backend?")




