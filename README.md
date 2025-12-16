**Insurance Cost Estimator**
An Explainable Machine Learning Application for Insurance Cost Awareness
1. **Executive Summary**

The Insurance Cost Estimator is an explainable machine learning application designed to improve public understanding of health insurance cost drivers.
Rather than generating insurance quotes, the system provides indicative cost estimates alongside clear explanations of the factors that most strongly influence those estimates.

The application is:

Phone-first and browser-based

Intended strictly for awareness and education, not underwriting

**Important:**
*All outputs are estimates for informational purposes only.*
*Final insurance pricing is determined exclusively by licensed insurers in accordance with regulatory guidelines.*

2. **Problem Context and Motivation**

Health insurance pricing is often opaque to end users. Many individuals are unable to clearly explain:

*Why their insurance costs differ from others?*

*Which factors genuinely increase costs?*

*Which factors matter less than commonly assumed?*

*What aspects of their profile are modifiable?*

This lack of transparency creates information asymmetry between insurers and the public.
The objective of this project is to reduce that gap by translating data-driven insights into simple, understandable explanations accessible to non-technical users.

3. **Analytical Questions Addressed**

This project is structured around three core questions:

How much might insurance cost based on a basic personal profile?

Which factors most strongly influence insurance costs?

Which factors contribute marginally and are often overestimated?

4. **Dataset Description**
**Source and Scope**

Source: *Public open-source insurance dataset (Kaggle)*

Records: *1,338 individuals*

Data quality: *No missing values in core numerical features*

The dataset was selected for its clarity, completeness, and suitability for explainable modeling.

**Features Used and Their Rationale**

**Age**
Age captures lifecycle-related risk. In the model, age contributes to a gradual increase in estimated cost but does not dominate predictions on its own. This reflects real-world insurance logic where age matters, but rarely explains extreme costs alone.

**Body Mass Index (BMI) (calculated from height and weight)**
BMI is used as a health-risk proxy, not a medical diagnosis. Higher BMI values are associated with increased insurance costs in the dataset and play a strong secondary role after lifestyle factors.

**Smoking Status**
Smoking status emerges as the single most influential factor in the analysis. Both EDA and model feature importance confirm that smoking significantly shifts cost distributions upward.

**Number of Dependants**
The number of dependants introduces additional coverage obligations. Its effect is moderate, increasing costs incrementally rather than dramatically.

**Sex (Internal Use Only)**
Included for model completeness but deliberately excluded from user-facing explanations due to its minimal influence and potential bias implications.

**Region (Internal Use Only)**
Used to capture contextual variation but shown to have low explanatory power relative to health and lifestyle factors.

No personal identifiers, income data, medical histories, or sensitive attributes are used at any stage.

5. **Methodological Approach**
5.1 **Problem Framing**

Initial framing focused on:

Ethical feature selection

Regulatory awareness

Explainability requirements

Accessibility for non-technical users

5.2 **Exploratory Data Analysis (EDA)**

EDA revealed several key patterns:

Insurance costs are highly right-skewed

Most individuals fall within low-to-mid cost ranges

A small subset of high-risk profiles accounts for extreme costs

Lifestyle-related factors dominate demographic variables

These findings directly informed feature selection and modeling choices.

5.3 **Modeling Strategy**

Two models were developed and evaluated:

**Linear Regression**
Used as a transparent baseline to understand linear relationships and coefficient behavior.

**Random Forest Regressor (Final Model)**
Selected as the primary model due to its ability to capture non-linear interactions while remaining interpretable through feature importance analysis.

Performance (Random Forest):

Mean Absolute Error (MAE): ~2,530

R² Score: ~0.86

This balance of performance and interpretability is critical for regulated domains such as insurance.

6. **Explainability and Key Insights**

Feature importance analysis highlights:

Smoking status as the dominant cost driver

BMI as a strong secondary contributor

Age as a steady but non-dominant factor

Dependants as a moderate influence

Region and sex as marginal contributors

**Key insight:**
Insurance cost variation is driven far more by modifiable lifestyle and health proxies than by demographic attributes.

7. **Application Design and User Experience**

The application is intentionally minimalist:

Vertical layout optimized for mobile screens

Minimal required inputs

Automatic BMI calculation

Plain-language explanations accompanying estimates

*Outputs include:*

Estimated annual cost (KES)

A range to reduce false certainty

Clear explanations of influencing factors

The system avoids exposing technical details, model internals, or statistical jargon.

8. **Responsible AI and Ethics**

This project adheres to responsible AI principles by:

Avoiding sensitive or invasive features

Prioritizing explainability over automation

Clearly communicating uncertainty

Including visible regulatory disclaimers

The application supports informed awareness, not decision automation.

9. **Technology Stack (and How It Was Used)**

*Python 3.11*
Serves as the core runtime, chosen for stability and compatibility with deployment environments.

*pandas & numpy*
Used for data cleaning, transformation, and numerical operations during EDA and modeling.

*scikit-learn*
Provided the modeling framework, including preprocessing pipelines, regression models, and evaluation metrics.

*joblib*
Used to serialize and persist the trained machine learning model for deployment.

*matplotlib*
Supported exploratory visualization during EDA to uncover distributional and relational patterns.

*Streamlit*
Enabled rapid development of a phone-friendly, interactive web application without frontend complexity.

10. **Local Execution**
pip install -r requirements.txt
streamlit run app.py

11. **Deployment Status**

Deployed and accessible via standard web browsers (desktop and mobile)

12. **Social Impact**

Improves insurance literacy

Reduces pricing confusion

Encourages informed financial planning

Professional Impact

Demonstrates end-to-end data science capability

Shows ethical ML application in a regulated context

Highlights strong communication of technical insights

13. **Disclaimer**

This application provides indicative estimates only for awareness and educational purposes.
Final insurance pricing decisions are made solely by licensed insurers under applicable regulatory frameworks.

14. **Author**

Benuel Omanga

Master’s in Data Science & Business Analytics

Focus: *Explainable ML, Applied Analytics, Social Corporate Responsibility*
