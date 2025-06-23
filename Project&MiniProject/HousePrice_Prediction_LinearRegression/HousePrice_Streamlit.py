import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

# Train model 
@st.cache_data
def train_model():
    np.random.seed(42)
    n = 1000
    square_feet = np.random.randint(400, 3500, n)
    bedrooms = np.random.randint(1, 6, n)
    bathrooms = np.random.randint(1, 4, n)
    location_score = np.random.uniform(3, 10, n)
    age = np.random.randint(0, 40, n)

    price = (
        square_feet * 320 +
        bedrooms * 60000 +
        bathrooms * 45000 +
        location_score * 120000 -
        age * 9000 +
        np.random.normal(0, 60000, n)
    )

    df = pd.DataFrame({
        'SquareFeet': square_feet,
        'Bedrooms': bedrooms,
        'Bathrooms': bathrooms,
        'LocationScore': location_score,
        'Age': age,
        'Price': price
    })

    X = df[['SquareFeet', 'Bedrooms', 'Bathrooms', 'LocationScore', 'Age']]
    y = df['Price']

    model = LinearRegression()
    model.fit(X, y)
    return model

model = train_model()

# Streamlit UI
st.title("🏠 House Price Predictor")
st.write("Enter house features below to predict the price:")

square_feet = st.slider("Square Feet", 400, 3500, 1200)
bedrooms = st.selectbox("Number of Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.selectbox("Number of Bathrooms", [1, 2, 3])
location_score = st.slider("Location Score (1-10)", 1.0, 10.0, 7.0, step=0.1)
age = st.slider("Age of House (Years)", 0, 40, 10)

if st.button("Predict Price"):
    features = np.array([[square_feet, bedrooms, bathrooms, location_score, age]])
    prediction = model.predict(features)[0]
    st.success(f"Estimated Price: ₹{prediction:,.2f}")