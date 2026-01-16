### Insurance Premium Prediction
An end-to-end Machine Learning project that predicts insurance premium categories (Low / Medium / High) based on demographic and lifestyle information.

# Overview
Insurance companies charge an annual payment called an insurance premium. The amount depends on factors like age, income, lifestyle, and health indicators. This project builds a classification model to categorize customers into premium tiers, helping both insurers and users make data-driven decisions.

Key Features:

Advanced feature engineering for better risk assessment

Random Forest classification model

FastAPI backend with full validation

Streamlit frontend for easy interaction

Production-ready pipeline

# Problem Statement
Given user attributes:

Age

Height (meters)

Weight (kg)

Annual Income (LPA - Lakhs Per Annum)

Smoking status (boolean)

City (string)

Occupation (string)

Predict the insurance premium category:

Low

Medium

High

Benefits:

For insurance companies: Segment customers by risk and payment capacity

For users: Understand premium category and make informed lifestyle decisions

# Feature Engineering
Instead of raw features, engineered features better represent real-world risk factors:

1. Age Group (Categorical)

python
if age < 25:
    return "young"
elif age < 45:
    return "adult"
elif age < 60:
    return "middle_aged"
else:
    return "senior"

2. BMI (Body Mass Index)

text
bmi = weight / (height ** 2)
Captures health risk more effectively than weight alone.

3. Lifestyle Risk (Derived Feature)

Combines BMI and smoking status:

python
if smoker and bmi > 30:
    return "high"
elif smoker or bmi > 27:
    return "medium"
else:
    return "low"

4. City Tier Classification

Cities grouped into tiers:

Tier 1: Major metropolitan cities (Mumbai, Delhi, Bangalore, etc.)

Tier 2: Developing cities

Tier 3: Other cities

5. Direct Features

income_lpa

occupation

# Model Details
Algorithm: Random Forest Classifier

Preprocessing:

One-Hot Encoding for categorical features (Age Group, Occupation, City Tier, Lifestyle Risk)

Numerical features passed directly

Pipeline: Feature preprocessing + model combined using sklearn.pipeline

# API Documentation
Base URL
text
http://localhost:8000
Example Request
json
{
  "age": 30,
  "weight": 65,
  "height": 1.7,
  "income_lpa": 10,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}

Example Response
json
{
  "predicted_category": "Medium",
  "confidence": 0.84,
  "class_probabilities": {
    "Low": 0.10,
    "Medium": 0.84,
    "High": 0.06
  }
} 

# Project Structure
text
insurance-premium-prediction/
├── app.py                      # FastAPI application
├── model/                      # Trained model files
│   ├── model.pkl
│   └── preprocessor.pkl
├── schema/                     # Pydantic schemas
│   └── schemas.py
├── config/                     # Configuration files
│   └── settings.py
├── frontend/                   # Streamlit UI
│   └── streamlit_app.py
├── training/                   # Training scripts
│   └── train_model.py
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── .gitignore

# Installation & Setup

1. Clone the Repository
bash
git clone https://github.com/BeyzaAkgun/insurance-premium-prediction.git
cd insurance-premium-prediction
2. Create Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
pip install -r requirements.txt
4. Download/Place Model Files
Ensure the trained model files (model.pkl and preprocessor.pkl) are in the model/ directory.

#  Usage
Backend (FastAPI)
bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
API Documentation: http://localhost:8000/docs

Swagger UI: http://localhost:8000/docs



Frontend (Streamlit)
bash
streamlit run frontend/streamlit_app.py
Frontend URL: http://localhost:8501

#  Endpoints
1. Health Check
text
GET /health
Response:

json
{"status": "healthy", "timestamp": "2024-01-01T12:00:00Z"}

2. Predict Premium Category
text
POST /predict
Request Body: See Example Request

3. Model Information
text
GET /model-info
Response: Model version, algorithm, and training date

#  Frontend (Streamlit)
The Streamlit UI provides an intuitive interface where users can:

Input their details using forms and sliders

Instantly see predicted premium category

View model confidence scores

See probability distribution across all categories

Get explanations for the prediction

