# Business Insights Report – Customer Spending Prediction

## 1. Project Objective
The objective is to classify customers into Low, Medium, and High spending categories using demographic and annual income information.

## 2. Dataset
The project uses the Mall Customer Segmentation dataset containing customer demographic and spending-related information.

## 3. Data Preparation
- Checked missing values and duplicate records.
- Standardized column names.
- Converted numeric columns to appropriate data types.
- Created spending categories from the original spending score.
- Excluded CustomerID and Spending Score from model inputs to avoid irrelevant identifiers and target leakage.

## 4. Exploratory Data Analysis
The analysis includes:
- Spending category distribution.
- Customer age distribution.
- Annual income versus spending score.
- Gender distribution.
- Annual income distribution across spending categories.

## 5. Machine Learning Models
Two classification models were trained:
1. Logistic Regression
2. Random Forest Classifier

## 6. Model Evaluation
The models were compared using:
- Accuracy
- Weighted Precision
- Weighted Recall
- Weighted F1-score
- Confusion Matrix

The best model was selected based on weighted F1-score.

## 7. Business Applications
The resulting predictions may help demonstrate how a business could:
- Explore customer spending segments.
- Design different marketing campaigns for different predicted groups.
- Identify customer groups for further analysis.
- Support data-driven customer engagement strategies.

## 8. Limitations
- The dataset is relatively small.
- The spending categories are created using predefined score ranges.
- The model uses only gender, age, and annual income.
- Predictions are educational estimates and should not be treated as actual customer behaviour or used alone for business decisions.

## 9. Conclusion
The project demonstrates the complete basic machine learning workflow, from data preparation to model comparison and customer prediction.