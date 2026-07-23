# 🩺 Diabetes Risk Prediction - End-to-End Machine Learning Capstone

**AnalystLab Africa Machine Learning Internship | Capstone Project**  
**Author:** Ethel Kuvirima  
**Deployment Link:** [Streamlit Live App](https://your-app-link.streamlit.app)  

---

## 📌 Project Overview
This project applies the complete machine learning workflow to predict diabetes risk using patient health diagnostic indicators. Early detection allows for timely lifestyle and medical intervention, reducing long-term health complications.

## 📊 Dataset Information
- **Source:** [Pima Indians Diabetes Dataset on Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Instances:** 768 patient records
- **Features:** 8 clinical features including Glucose, Blood Pressure, BMI, Insulin, Age, etc.
- **Target Variable:** `Outcome` (0 = No Diabetes, 1 = Diabetes)

## 🛠️ Project Workflow
1. **Data Preprocessing:** Handled physiologically impossible zero values across health metrics using median imputation.
2. **Exploratory Data Analysis (EDA):** Analyzed feature distributions, outliers, and correlation matrix heatmaps.
3. **Feature Scaling:** Standardized numerical attributes using `StandardScaler`.
4. **Model Development:** Trained and evaluated multiple classification models:
   - Logistic Regression
   - Random Forest Classifier
   - XGBoost Classifier
5. **Evaluation Strategy:** Focused on **Recall** and **F1-Score** to minimize false negatives in medical screening.
6. **Deployment:** Built and hosted an interactive Streamlit application.

## 🏆 Model Performance Summary

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | 77.2% | 0.71 | 0.61 | 0.66 | 0.82 |
| **XGBoost Classifier** | 76.6% | 0.68 | 0.65 | 0.66 | 0.81 |
| **Random Forest (Best)** | **79.2%** | **0.73** | **0.68** | **0.70** | **0.84** |

## 💡 Key Clinical Insights
- **Glucose Level** and **BMI** are the strongest predictors of diabetes risk.
- Age shows a strong correlation with risk, peaking between 40 and 60 years old.

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/pacesetter130804/analystlab-deployment.git](https://github.com/pacesetter130804/analystlab-deployment.git)
   cd analystlab-deployment
