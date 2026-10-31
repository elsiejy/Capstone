import streamlit as st
import joblib
import pandas as pd

# Load the saved Random Forest model and the column list it was trained on
@st.cache_resource
def load_model():
    return joblib.load("cancellation_model.pkl")

saved = load_model()
model = saved["model"]
model_columns = saved["columns"]

st.title("🏨 Hotel Booking Cancellation Predictor")
st.write("Enter the booking details to predict whether the guest is likely to cancel. "
         "Model: Random Forest (79.6% accuracy on test data).")

# Input fields: the same 5 features used to train the model in Google Colab
deposit_type = st.selectbox("Deposit type", ["No Deposit", "Non Refund", "Refundable"])
lead_time = st.number_input("Lead time (days between booking and arrival)",
                            min_value=0, max_value=737, value=200, step=1)
market_segment = st.selectbox("Market segment", ["Online TA", "Offline TA/TO", "Groups", "Direct",
                                                 "Corporate", "Complementary", "Aviation"])
total_of_special_requests = st.number_input("Number of special requests",
                                            min_value=0, max_value=5, value=0, step=1)
hotel = st.selectbox("Hotel", ["City Hotel", "Resort Hotel"])

if st.button("Predict"):
    # 1. Arrange inputs into a dictionary using the original dataset column names
    input_dict = {
        "deposit_type": [deposit_type],
        "lead_time": [lead_time],
        "market_segment": [market_segment],
        "total_of_special_requests": [total_of_special_requests],
        "hotel": [hotel],
    }

    # 2. Convert to a DataFrame and one-hot encode it exactly like in Colab
    input_df = pd.DataFrame(input_dict)
    input_df = pd.get_dummies(input_df, dtype=int).reindex(columns=model_columns, fill_value=0)

    # 3. Predict the chance of cancellation
    prob = model.predict_proba(input_df)[0, 1]

    st.metric("Chance this booking will be cancelled", f"{prob:.0%}")
    if prob >= 0.5:
        st.error("Likely to cancel. Consider asking for a deposit or sending reconfirmation reminders.")
    else:
        st.success("Likely to keep the booking.")
