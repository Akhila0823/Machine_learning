import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f4f4f4;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            max-width: 500px;
            margin: auto;
        }
        h1 {
            text-align: center;
            color: #4B8BBE;
        }
        .stButton > button {
            background-color: #4B8BBE;
            color: white;
            font-size: 16px;
            padding: 0.5em 1.5em;
            border-radius: 8px;
            border: none;
        }
        .stButton > button:hover {
            background-color: #306998;
        }
    </style>
""", unsafe_allow_html=True)

# Page layout
st.markdown('<div class="main">', unsafe_allow_html=True)

# Title
st.markdown("<h1>TV Budget → Sales Predictor</h1>", unsafe_allow_html=True)

# Input field
tv_budget = st.number_input("📺 Enter TV Marketing Budget ($):", min_value=0.0, step=0.1)

# Predict Button
if st.button("Predict Sales"):
    prediction = model.predict(np.array([[tv_budget]]))
    st.success(f"📈 Predicted Sales: **{prediction[0]:.2f} units**")

# End layout div
st.markdown('</div>', unsafe_allow_html=True)

