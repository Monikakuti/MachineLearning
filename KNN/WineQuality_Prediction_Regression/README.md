# 🍷 Wine Quality Prediction using KNN Regressor

This mini project uses **K-Nearest Neighbors Regression (KNN)** to predict the **quality score** of red wine based on its chemical properties.

---

## 📊 Features

| Feature               | Description                          |
|------------------------|--------------------------------------|
| fixed acidity          | Non-volatile acids in wine           |
| volatile acidity       | Acetic acid amount (vinegar taste)   |
| citric acid            | Gives wine freshness                 |
| residual sugar         | Sugar left after fermentation        |
| chlorides              | Saltiness of the wine                |
| free sulfur dioxide    | Free form of SO₂ for preservation    |
| total sulfur dioxide   | Total SO₂ content                    |
| density                | Density of the wine                  |
| pH                     | Acidity/alkalinity level             |
| sulphates              | Preservative, adds bitterness        |
| alcohol                | Alcohol percentage                   |
| **quality (target)**   | Wine quality score (0 to 10)         |

---

## 🎯 Objective

- Predict the **quality** of wine using **KNN Regressor**
- Evaluate with `R² Score` and `Mean Squared Error`
- Visualize the relationship between **alcohol** and **predicted quality**

---

## 🧪 Model Used

- **KNeighborsRegressor** from Scikit-learn
- Tried different `k` values (like 3, 5, 7) to compare performance
- Visualization used `matplotlib`

---

## 🔍 Evaluation Metrics

- **Mean Squared Error (MSE)**: Measures average error size
- **R² Score**: Shows how well the model explains variability

---

## 📈 Visualization

We created a regression-style plot:

- X-axis: `alcohol %`
- Y-axis: Predicted wine `quality`
- Green line: Predicted quality from KNN
- Red dots: Actual wine quality data

---

## 🧠 Learnings

- KNN can be used for **regression**, not just classification
- Best results depend on choosing a proper `k` value
- Some features (like alcohol) show strong trends with quality

---
