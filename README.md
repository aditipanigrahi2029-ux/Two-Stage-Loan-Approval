
# 🏦 Two-Stage Loan Approval Prediction System

An end-to-end Machine Learning application that predicts loan approval status and estimates the loan amount using Random Forest models.

## 🚀 Project Overview

The application uses a two-stage ML pipeline:

- **Stage 1 — Loan Approval Prediction:** A Random Forest Classifier predicts whether a loan application is approved or rejected.
- **Stage 2 — Loan Amount Prediction:** If approved, a Random Forest Regressor predicts the loan amount.

## 🛠️ Tech Stack

- **Python, Pandas, Scikit-learn** — Data preprocessing and machine learning
- **FastAPI** — REST API backend
- **Streamlit** — Interactive frontend
- **Joblib** — Saving and loading trained ML models
- **Docker** — Application containerization
- **Docker Hub** — Image distribution

## ⚙️ How It Works

1. The user enters applicant details through Streamlit.
2. Streamlit sends the data to the FastAPI backend.
3. The classification model predicts loan approval status.
4. If approved, the regression model predicts the loan amount.
5. The prediction is displayed in the Streamlit application.

## 🐳 Run Using Docker

Make sure Docker is installed and running.

### Step 1: Pull the Docker Image

```bash
docker pull aditipanigrahi/loan-approval-app:1.0
```

### Step 2: Run the Container

```bash
docker run -d --name loan-app -p 8501:8501 aditipanigrahi/loan-approval-app:1.0
```

### Step 3: Open the Application

Visit: http://localhost:8501

## 📂 Project Structure

```text
Two-Stage-Loan-Approval/
├── api.py              # FastAPI backend
├── app.py              # Streamlit frontend
├── loan.py             # ML prediction logic
├── start.py            # Starts backend and frontend
├── Dockerfile          # Docker image configuration
├── requirements.txt    # Python dependencies
├── data/               # Trained ML model files
└── README.md           # Project documentation
```

## 🔗 Docker Hub

[View Docker Image](https://hub.docker.com/r/aditipanigrahi/loan-approval-app)

## 📚 Key Learnings

- Building a two-stage machine learning pipeline
- Integrating ML models with FastAPI
- Developing a Streamlit frontend
- Containerizing a complete application with Docker
- Publishing Docker images to Docker Hub

## 🙏 Acknowledgements

Special thanks to **CampusX** for explaining Docker fundamentals, and **Monal Singh** and **Krish Naik Academy** for project inspiration and learning resources.

## 👩‍💻 Author

**Aditi Panigrahi**
  
