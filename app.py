from pathlib import Path
import json
import joblib
import pandas as pd
import streamlit as st

# -----------------------------------
# PROJECT CONFIGURATION
# -----------------------------------

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "best_customer_spending_model.joblib"
DATA_PATH = BASE_DIR / "data" / "cleaned_customer_data.csv"
EVALUATION_PATH = BASE_DIR / "reports" / "model_evaluation.json"

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="Customer Spending Predictor",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ AI-Based Customer Spending Prediction")
st.write(
    "Predict customer spending categories using Machine Learning."
)

st.caption(
    "Final project | Veda Technology Internship | Day 34"
)

# -----------------------------------
# LOAD TRAINED MODEL
# -----------------------------------

@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        return None
    return joblib.load(MODEL_PATH)

model = load_model()

if model is None:
    st.error(
        "Trained model not found. Please train and save the model "
        "from the Jupyter Notebook first."
    )
    st.stop()

st.success("Machine Learning model loaded successfully.")

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.header("Navigation")

page = st.sidebar.radio(
    "Select a section",
    [
        "Single Customer Prediction",
        "Batch Customer Prediction",
        "Project Insights",
        "About Project"
    ]
)

# -----------------------------------
# SINGLE CUSTOMER PREDICTION
# -----------------------------------

if page == "Single Customer Prediction":

    st.header("Predict Spending Category")

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

    with col2:
        age = st.number_input(
            "Customer Age",
            min_value=18,
            max_value=100,
            value=25
        )

    with col3:
        income = st.number_input(
            "Annual Income (k$)",
            min_value=0.0,
            max_value=200.0,
            value=50.0,
            step=1.0
        )

    if st.button("Predict Spending Category", type="primary"):

        customer = pd.DataFrame({
            "Gender": [gender],
            "Age": [age],
            "Annual_Income": [income]
        })

        prediction = model.predict(customer)[0]

        st.subheader("Prediction Result")

        if prediction == "High":
            st.success(f"Predicted Category: {prediction}")
        elif prediction == "Medium":
            st.info(f"Predicted Category: {prediction}")
        else:
            st.warning(f"Predicted Category: {prediction}")

        # Display prediction probabilities if supported
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(customer)[0]
            classes = model.classes_

            probability_df = pd.DataFrame({
                "Category": classes,
                "Probability (%)": probabilities * 100
            })

            st.subheader("Prediction Probabilities")

            st.bar_chart(
                probability_df.set_index("Category")
            )

            st.dataframe(
                probability_df.round(2),
                use_container_width=True
            )

# -----------------------------------
# BATCH CUSTOMER PREDICTION
# -----------------------------------

elif page == "Batch Customer Prediction":

    st.header("Predict Multiple Customers")

    st.write(
        "Upload a CSV file containing Gender, Age, and Annual_Income."
    )

    sample_data = pd.DataFrame({
        "Gender": ["Male", "Female"],
        "Age": [25, 35],
        "Annual_Income": [40, 70]
    })

    st.download_button(
        "Download Sample CSV",
        data=sample_data.to_csv(index=False),
        file_name="sample_customers.csv",
        mime="text/csv"
    )

    uploaded_file = st.file_uploader(
        "Upload Customer CSV",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:
            customers = pd.read_csv(uploaded_file)

            required_columns = [
                "Gender",
                "Age",
                "Annual_Income"
            ]

            missing_columns = [
                col for col in required_columns
                if col not in customers.columns
            ]

            if missing_columns:
                st.error(
                    f"Missing columns: {missing_columns}"
                )

            else:
                input_data = customers[required_columns].copy()

                predictions = model.predict(input_data)

                result = customers.copy()

                result["Predicted_Spending_Category"] = predictions

                st.success(
                    f"Predictions generated for {len(result)} customers."
                )

                st.dataframe(
                    result,
                    use_container_width=True
                )

                st.download_button(
                    "Download Prediction Results",
                    data=result.to_csv(index=False),
                    file_name="customer_predictions.csv",
                    mime="text/csv"
                )

        except Exception as error:
            st.error(f"Unable to process CSV: {error}")

# -----------------------------------
# PROJECT INSIGHTS
# -----------------------------------

elif page == "Project Insights":

    st.header("Customer Data Insights")

    if DATA_PATH.exists():

        df = pd.read_csv(DATA_PATH)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Customers", len(df))

        with col2:
            if "Age" in df.columns:
                st.metric(
                    "Average Age",
                    round(df["Age"].mean(), 1)
                )

        with col3:
            if "Annual_Income" in df.columns:
                st.metric(
                    "Average Annual Income",
                    f"{df['Annual_Income'].mean():.1f} k$"
                )

        if "Spending_Category" in df.columns:

            st.subheader("Spending Category Distribution")

            category_counts = (
                df["Spending_Category"]
                .value_counts()
            )

            st.bar_chart(category_counts)

        if (
            "Annual_Income" in df.columns
            and "Spending_Category" in df.columns
        ):
            st.subheader("Average Income by Spending Category")

            income_summary = (
                df.groupby("Spending_Category")["Annual_Income"]
                .mean()
            )

            st.bar_chart(income_summary)

    else:
        st.warning(
            "Cleaned dataset not found. Add the CSV file to the data folder."
        )

    # Model evaluation information
    if EVALUATION_PATH.exists():

        st.subheader("Model Evaluation Results")

        with open(EVALUATION_PATH, "r") as file:
            evaluation = json.load(file)

        st.json(evaluation)

# -----------------------------------
# ABOUT PROJECT
# -----------------------------------

elif page == "About Project":

    st.header("About This Project")

    st.markdown("""
    ### AI-Based Customer Spending Prediction

    This application uses Machine Learning to classify customers
    into three spending categories:

    - Low Spending
    - Medium Spending
    - High Spending

    ### Input Features

    - Gender
    - Age
    - Annual Income

    ### Machine Learning Models

    - Logistic Regression
    - Random Forest Classifier

    ### Technologies

    - Python
    - Pandas
    - Scikit-learn
    - Streamlit
    - Joblib

    ### Project Objective

    To demonstrate a complete beginner-friendly Machine Learning
    workflow, from data preparation and model evaluation to
    interactive predictions.
    """)

st.divider()

st.caption(
    "Developed as part of the Veda Technology Internship."
)