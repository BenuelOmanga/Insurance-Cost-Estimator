Insurance Cost Estimator (Explainable ML Project)
Project Overview

This project is an explainable insurance cost estimation tool designed to improve public understanding of what influences health insurance costs. The application provides indicative estimates and clear explanations of key cost drivers using machine learning, with a strong focus on transparency, ethics, and accessibility.

The tool is built to be mobile-friendly, allowing everyday users to access it from a normal phone browser without technical knowledge.

⚠️ This project does not provide insurance quotes or pricing. All outputs are estimates for awareness and educational purposes only.

Problem Motivation

Many individuals struggle to understand why health insurance costs differ widely between people with similar circumstances. Insurance pricing models are often complex and opaque, leaving users unable to identify:

What factors increase their insurance costs

Which factors help keep costs lower

What aspects they can realistically influence

This project addresses that gap by using data analytics and explainable machine learning to surface clear, data-driven insights in simple language.

Key Questions Addressed

How much might insurance cost based on a person’s profile?

Which factors influence insurance costs the most?

Which changes are associated with lower or higher costs?

Dataset

Source: Public open-source insurance dataset (Kaggle)

Records: 1,338

Features used:

Age

BMI (calculated from height and weight)

Smoking status

Number of dependants

Sex (internal use only)

Region (internal use only)

No personal identifiers, medical records, or sensitive data are used.

Methodology
Phase 1 – Problem Framing

Defined the real-world problem, target users, ethical boundaries, and regulatory considerations.

Phase 2 – Exploratory Data Analysis (EDA)

Key findings:

Insurance costs are highly skewed: most individuals pay moderate amounts, while a small group accounts for very high costs.

Smoking is the strongest driver of increased insurance costs.

BMI shows a strong association with higher costs and acts as a health-risk proxy.

Age increases costs gradually but does not explain large differences on its own.

Number of dependants has a moderate effect.

Region and gender have minimal influence.

Phase 3 – Modeling

Baseline Model: Linear Regression (for transparency)

Primary Model: Random Forest Regressor (for improved accuracy)

Performance (Random Forest):

MAE ≈ 2,530

R² ≈ 0.86

The final system balances predictive performance with interpretability, which is critical in regulated domains such as insurance.

Key Insights (Model + EDA)

Lifestyle-related factors dominate insurance cost estimation more than demographic traits.

Smoking alone explains a large proportion of cost variation across individuals.

Maintaining a healthy BMI is strongly associated with lower estimated insurance costs.

Age contributes steadily but is not a dominant cost driver by itself.

Region and gender contribute minimally, reducing the risk of demographic bias.

These insights are explicitly translated into user-facing explanations within the application.

Impact
Social & Practical Impact

Improves insurance literacy among everyday users.

Helps individuals understand why their insurance costs may be higher or lower.

Encourages informed lifestyle and financial planning decisions.

Reduces information asymmetry between insurers and the public.

Professional & Technical Impact

Demonstrates end-to-end data science skills: EDA → modeling → explainability → deployment.

Shows responsible AI practices in a regulated domain.

Highlights the ability to translate complex analytics into simple, actionable insights.

Strong portfolio example for roles in Data Science, Business Analytics, Risk Analytics, and FinTech.

Explainability & Ethics

Feature importance is explicitly analyzed and documented.

Lifestyle and health proxies dominate predictions, not sensitive demographics.

No income, occupation, or medical history is used.

Outputs are framed as estimates, never guarantees.

This design aligns with responsible AI principles and regulatory awareness.

Application Features

Phone-first, browser-based interface

Automatic BMI calculation

Clear explanations of what increases or reduces estimated cost

Estimated cost range to reduce false certainty

Regulatory and ethical disclaimer always visible

Technology Stack

Python

pandas, numpy

scikit-learn

joblib

Streamlit

How to Run Locally
pip install -r requirements.txt
streamlit run app.py

Deployment Status

🚀 Deployed and accessible via browser (desktop and mobile)

Disclaimer

This application provides indicative estimates only for awareness and educational purposes. Final insurance pricing is determined by licensed insurers in accordance with applicable regulatory guidelines. This tool does not replace professional insurance advice or underwriting processes.

Author

Benuel Omanga
Data Science & Business Analytics
Focused on explainable analytics, ethical ML, and real-world impact