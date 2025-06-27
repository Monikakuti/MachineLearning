# 🤖 Logistic Regression - Diabetes Prediction (Mini Project)

This mini machine learning project uses **Logistic Regression** to predict whether a patient has **diabetes** or not, based on medical data.

---

## 📁 Dataset

- **Link Used:** https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv  
- **Records:** 768 samples  
- **Target:** `Outcome` → 1 = Has diabetes, 0 = No diabetes

---

## 📊 Features

| Feature                     | Description                            |
|----------------------------|----------------------------------------|
| Pregnancies                | Number of times pregnant               |
| Glucose                    | Plasma glucose concentration           |
| BloodPressure              | Diastolic blood pressure (mm Hg)       |
| SkinThickness              | Skin fold thickness (mm)               |
| Insulin                    | 2-Hour serum insulin (mu U/ml)         |
| BMI                        | Body Mass Index (weight/height²)       |
| DiabetesPedigreeFunction   | Family history of diabetes             |
| Age                        | Age in years                           |
| **Outcome (Target)**       | 1 = Diabetes, 0 = No diabetes          |

---

## 🧠 Model Used

- **Algorithm:** Logistic Regression  
- **Library:** Scikit-learn  
- **Evaluation:** Accuracy, Confusion Matrix, Classification Report  

---

## 🧪 Workflow

1. Load dataset using Pandas
2. Split into train and test sets
3. Build Logistic Regression model
4. Predict and evaluate results
5. Visualize the confusion matrix

---

## 📈 Evaluation Metrics

- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**
- **Confusion Matrix**

---

## 🔍 Key Learnings

- Logistic Regression is best suited for **binary classification** (yes/no, 0/1).
- The **sigmoid function** maps inputs to probabilities between 0 and 1.
- Good feature scaling and cleaning are essential for model accuracy.

---
