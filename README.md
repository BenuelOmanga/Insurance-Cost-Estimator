Insurance Cost Estimator
An Explainable Machine Learning Application for Insurance Cost Awareness
1. Project Overview

The Insurance Cost Estimator is an explainable machine learning application designed to help individuals understand what factors influence health insurance costs.

Rather than producing insurance quotes, the tool provides indicative cost estimates and clear, human-readable explanations of the main drivers behind those estimates.

The application is:

Phone-first and accessible via a standard web browser

Built with responsible AI principles

Designed for public awareness, not underwriting or pricing

⚠️ All outputs are estimates for educational and awareness purposes only.
Final insurance pricing is determined by licensed insurers in line with regulatory guidelines.

2. Problem Context & Motivation

Insurance pricing is often perceived as opaque and difficult to understand. Many individuals are unable to answer basic questions such as:

Why does my insurance cost more than someone else’s?

Which factors matter the most?

What, if anything, can I change to reduce my cost?

This lack of transparency creates information asymmetry between insurers and consumers.

This project addresses that gap by combining:

Exploratory data analysis

Interpretable machine learning

A simple, mobile-friendly interface

The goal is understanding, not prediction alone.

3. Key Questions Addressed

How much might insurance cost based on a basic personal profile?

Which factors have the strongest influence on insurance costs?

Which factors contribute less than people commonly assume?

How can insights be communicated clearly to non-technical users?

4. Dataset

Source: Public open-source insurance dataset (Kaggle)

Records: 1,338 individuals

Data characteristics: Clean, no missing values in core features

Features Used

Age

Body Mass Index (BMI) (calculated from height and weight)

Smoking status

Number of dependants

Sex (internal use only)

Region (internal use only)

No personal identifiers, medical records, income data, or sensitive attributes are included.

5. Methodology
5.1 Problem Framing

Defined:

Target users (general public)

Ethical boundaries

Regulatory awareness

Explainability requirements

5.2 Exploratory Data Analysis (EDA)

Key findings from EDA include:

Insurance costs are highly right-skewed

Most individuals pay moderate costs

A small subset accounts for extremely high costs

Lifestyle and health-related factors dominate cost variation

EDA directly informed feature selection and modeling decisions.

5.3 Modeling Approach

Two models were trained and evaluated:

Model	Purpose
Linear Regression	Baseline & interpretability
Random Forest Regressor	Primary prediction model

Final model selection: Random Forest Regressor
Chosen for its ability to capture non-linear relationships while retaining interpretability via feature importance.

Model Performance (Random Forest)

MAE: ~2,530

R²: ~0.86

This indicates strong explanatory power without overfitting.

6. Explainability & Key Insights

Feature importance analysis reveals:

Primary Cost Drivers

Smoking status – strongest contributor to higher costs

BMI – strong health-risk proxy

Age – gradual, consistent increase

Secondary / Minor Factors

Number of dependants – moderate effect

Region & sex – minimal influence

Key Insight

Lifestyle and health-related factors explain far more cost variation than demographic attributes. This significantly reduces the risk of demographic bias.

7. Application Design
User Experience

Simple, vertical layout suitable for mobile phones

Minimal inputs

Automatic BMI calculation

Clear explanations alongside estimates

Output Design

Estimated annual cost (KES)

Estimated range to reduce false certainty

Plain-language explanations of key influencing factors

The application never exposes:

Model internals

Raw feature weights

Technical jargon

8. Responsible AI & Ethics

This project follows responsible AI practices:

No sensitive personal data used

No income or occupation features

No medical diagnoses

Outputs framed strictly as estimates

Clear regulatory disclaimer always visible

The system prioritizes explainability over automation.

9. Technology Stack

Python 3.11

pandas, numpy

scikit-learn

joblib

matplotlib

Streamlit

10. How to Run Locally
pip install -r requirements.txt
streamlit run app.py

11. Deployment Status

🚀 Deployed and accessible via browser (desktop & mobile)

12. Impact
Social Impact

Improves insurance literacy

Encourages informed decision-making

Reduces confusion around insurance pricing

Professional Impact

Demonstrates end-to-end data science workflow

Shows ethical ML in a regulated domain

Highlights ability to translate analytics into real-world tools

13. Disclaimer

This application provides indicative estimates only for awareness and educational purposes.
Final insurance pricing is determined exclusively by licensed insurers under applicable regulatory frameworks.

14. Author

Benuel Omanga
Master’s in Data Science & Business Analytics
Focus areas: Explainable ML, Responsible AI, Applied Analytics