import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title('House Price Predictor')

# Input fields
area = st.number_input('Area (sqft)')
bedrooms = st.number_input('Number of Bedrooms', step=1)
bathrooms = st.number_input('Number of Bathrooms', step=1)

# Predict button
if st.button('Predict'):
    input_data = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted House Price: ₹ {prediction:,.2f}")

