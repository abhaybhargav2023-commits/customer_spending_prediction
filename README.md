# AI-Based Customer Spending Prediction

## Project Overview
An end-to-end beginner-friendly machine learning classification project that predicts whether a customer belongs to a Low, Medium, or High spending category using demographic and annual income information.

## Objective
To understand and implement a complete machine learning workflow, including data cleaning, EDA, feature engineering, preprocessing, model training, evaluation, and prediction.

## Dataset
Mall Customer Segmentation Dataset.

Expected columns:
- CustomerID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

## Spending Categories
| Spending Score | Category |
|---|---|
| 1–39 | Low |
| 40–60 | Medium |
| 61–100 | High |

## Input Features and Target
**Input features (X):**
- Gender
- Age
- Annual Income

**Target (y):**
- Spending Category

The original Spending Score is excluded from the input features because it is used to create the target variable.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Joblib

## Project Workflow
1. Dataset loading and exploration.
2. Data cleaning and missing-value handling.
3. Exploratory Data Analysis.
4. Spending category creation.
5. Feature selection and preprocessing.
6. Train-test split.
7. Logistic Regression model training.
8. Random Forest model training.
9. Model comparison and evaluation.
10. Confusion matrix and feature importance.
11. Sample customer prediction.
12. Saving the trained model and cleaned dataset.

## Models Implemented
- Logistic Regression
- Random Forest Classifier

## Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## Project Outputs
- Cleaned customer dataset.
- EDA visualizations.
- Model performance comparison.
- Confusion matrix.
- Feature importance analysis.
- Saved trained model.
- Sample prediction function.
- Business insights report.

## How to Run

### 1. Clone the repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder
```bash
cd day_32_customer_spending_prediction
```

### 3. Create and activate a virtual environment
```bash
python -m venv .venv
```

Windows:
```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Add the dataset
Place `Mall_Customers.csv` inside the `data` directory.

### 6. Run the notebook
```bash
jupyter notebook
```

Open `notebooks/customer_spending_prediction.ipynb` and run all cells.

## Limitations
This is an educational classification project. Spending categories are derived from predefined spending-score ranges, and the model uses a limited set of customer attributes. Results should not be interpreted as guaranteed real-world spending behaviour.

## Conclusion
The project demonstrates how basic machine learning techniques can be used to explore customer data, classify spending categories, compare models, and generate sample predictions.
## Latest Project Updates – Day 33

The project was extended with additional machine learning evaluation, prediction, and documentation features.

### Additional Implementations

- Detailed model performance comparison.
- Accuracy, Precision, Recall, and F1-score analysis.
- Confusion matrix visualization.
- Random Forest feature importance analysis.
- Prediction probabilities for new customer records.
- Multiple customer spending predictions.
- Model persistence using Joblib.
- Loading and testing the saved machine learning model.
- Automated project deliverable verification.
- Business insights generated from customer data.

### Model Evaluation

Two classification algorithms were implemented and compared:

1. Logistic Regression
2. Random Forest Classifier

Evaluation metrics:
- Accuracy
- Weighted Precision
- Weighted Recall
- Weighted F1-score

The best-performing model is selected based on the actual weighted F1-score.

### Prediction Capabilities

The trained model accepts the following customer information:

- Gender
- Age
- Annual Income

It predicts one of three spending categories:

- Low
- Medium
- High

The project also provides class probability estimates for new customer records.

### Model Saving and Reusability

The trained model is saved using Joblib and can be loaded later without retraining.

### Additional Project Outputs

- Model comparison visualization.
- Confusion matrix.
- Feature importance chart.
- Model evaluation JSON file.
- Updated business insights report.

### Learning Outcomes – Day 33

- Learned detailed classification model evaluation.
- Understood confusion matrix interpretation.
- Explored feature importance.
- Implemented prediction probabilities.
- Tested multiple customer records.
- Learned model persistence and reusability.
- Improved project documentation and validation.
# AI-Based Customer Spending Prediction

An end-to-end Machine Learning project that predicts customer spending categories using customer demographic and annual income information. The project includes data preprocessing, exploratory data analysis, machine learning model training, evaluation, and an interactive Streamlit web application.

## 🚀 Live Application

**Live Demo:** https://customerspendingprediction-unique.streamlit.app/

## 📌 Project Overview

The objective of this project is to classify customers into three spending categories:

- Low Spending
- Medium Spending
- High Spending

The prediction is based on customer features such as Gender, Age, and Annual Income.

This solution can help businesses understand customer spending behaviour and support data-driven marketing and customer segmentation strategies.

## 🎯 Project Objectives

- Clean and prepare the customer dataset.
- Perform Exploratory Data Analysis (EDA).
- Create meaningful visualizations to identify customer patterns.
- Apply feature engineering and preprocessing.
- Train and evaluate at least two classification models.
- Compare models using Accuracy, Precision, Recall, and F1-score.
- Analyze the confusion matrix and feature importance.
- Build an interactive customer spending prediction dashboard.
- Enable individual and batch predictions.

## 📂 Dataset

**Dataset:** Mall Customer Segmentation Data

**Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

Features used:
- Gender
- Age
- Annual Income (k$)

Target variable:
- Spending Category (Low, Medium, High)

## 🛠️ Technologies & Tools

- Python
- Pandas & NumPy
- Matplotlib & Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook
- Git & GitHub

## ⚙️ Machine Learning Workflow

1. Data Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis
4. Feature Engineering
5. Train-Test Split
6. Classification Model Training
7. Model Evaluation and Comparison
8. Model Saving and Loading
9. Streamlit Application Development
10. Cloud Deployment

## 🤖 Machine Learning Models

The project uses classification algorithms to predict customer spending categories.

Model performance is evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## 💻 Application Features

- Interactive Streamlit dashboard.
- Individual customer spending prediction.
- Batch prediction using CSV upload.
- Prediction probability visualization.
- Customer spending insights.
- Downloadable prediction results.
- Input validation and preprocessing.

## 📁 Project Structure

```text
customer_spending_prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── Dockerfile
│
├── data/
│   ├── Mall_Customers.csv
│   └── cleaned_customer_data.csv
│
├── notebooks/
│   └── customer_spending_prediction.ipynb
│
├── models/
│   └── best_customer_spending_model.joblib
│
├── reports/
│   └── business_insights_report.md
│
├── visualizations/
│
└── .streamlit/
    └── config.toml
```

*Note: The structure above describes the intended project organization. Keep only files and folders that actually exist in your repository.*

## ▶️ Run Locally

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd customer_spending_prediction
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate