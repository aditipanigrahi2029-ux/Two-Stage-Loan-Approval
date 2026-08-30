
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import pandas as pd
# from loan import LoanApprovalApp
# # uvicorn api:app --reload
# app = FastAPI(
#     title="Loan Approval API",
#     description="Two-Stage ML API for predicting loan approval and amount."
# )

# model = LoanApprovalApp()

# class ApplicantData(BaseModel):
#     no_of_dependents: int
#     education: str
#     self_employed: str
#     income_annum: float
#     loan_amount: float
#     loan_term: int
#     cibil_score: int
#     residential_assets_value: float
#     commercial_assets_value: float
#     luxury_assets_value: float
#     bank_asset_value: float

# @app.post("/predict")
# def predict_loan(data : ApplicantData):
#     try:
#         applicant_df = pd.DataFrame([data.model_dump()])
#         result = model.two_stage_predict(applicant_df)

#         return {
#             "status": "success",
#             "data": result
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

from loan import LoanApprovalApp


# --------------------------------------------------
# 1. Create FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="Loan Approval API",
    description="Two-Stage ML API for predicting loan approval and loan amount."
)


# --------------------------------------------------
# 2. Load ML models
# --------------------------------------------------

# LoanApprovalApp loads both:
# Stage 1 -> Random Forest Classifier
# Stage 2 -> Random Forest Regressor

model = LoanApprovalApp()


# --------------------------------------------------
# 3. Input data format
# --------------------------------------------------

class ApplicantData(BaseModel):

    no_of_dependents: int
    education: str
    self_employed: str
    income_annum: float
    loan_amount: float
    loan_term: int
    cibil_score: int
    residential_assets_value: float
    commercial_assets_value: float
    luxury_assets_value: float
    bank_asset_value: float


# --------------------------------------------------
# 4. Prediction API endpoint
# --------------------------------------------------

@app.post("/predict_loan")
def predict_loan(data: ApplicantData):

    try:

        # ------------------------------------------
        # Convert API input into dictionary
        # ------------------------------------------

        input_data = data.model_dump()

        print("\n========== API INPUT ==========")
        print(input_data)


        # ------------------------------------------
        # Convert dictionary into DataFrame
        # ------------------------------------------

        applicant_df = pd.DataFrame([input_data])

        print("\n========== DATAFRAME ==========")
        print(applicant_df)


        # ------------------------------------------
        # Send DataFrame to loan.py
        # ------------------------------------------

        result = model.two_stage_predict(applicant_df)

        print("\n========== MODEL RESULT ==========")
        print(result)


        # ------------------------------------------
        # Convert loan.py result into API result
        # ------------------------------------------

        response = {
            "loan_status": result["approve"],
            "regression_prediction": result["regression_prediction"]
        }


        print("\n========== API RESPONSE ==========")
        print(response)


        # ------------------------------------------
        # Send result back to Streamlit
        # ------------------------------------------

        return response


    except Exception as e:

        print("\n========== BACKEND ERROR ==========")
        print(str(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )