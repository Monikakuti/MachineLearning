# 🫀 Heart Disease Prediction (Using Linear Regression)

This mini project uses **Linear Regression** to explore how **age** relates to the likelihood of heart disease.

> 🔎 Note: Even though this is a classification problem (0 or 1), Linear Regression is used **only for learning and visualization** purposes here.

---

## 📊 Dataset

The dataset includes medical records with features such as:
- `age`: Age of the patient
- `sex`: Gender (1 = male, 0 = female)
- `cp`: Chest pain type
- `chol`: Cholesterol level
- `thalachh`: Max heart rate
- `oldpeak`: Depression during exercise
- ... and more

The **target column** is:
- `output`: 1 = has heart disease, 0 = no heart disease

---

## 🎯 Goal

To observe the **linear relationship** between `age` and heart disease presence (`output`) using a straight-line fit.

---

## 🧰 Tools Used

- Python
- Pandas
- Scikit-learn
- Matplotlib

---

## 🔧 Steps Performed

1. Loaded the heart disease dataset
2. Selected `'age','sex','cp','thalach','exang','oldpeak','ca','thal'` as the features
3. Trained a **Linear Regression model** to predict `output`
4. Visualized: (only used 'age')
   - Actual data points (`output` values)
   - Linear trend line

---

## 📈 Visualization

The scatter plot shows:
- Red dots = real patient data (has disease or not)
- Green line = linear model trying to fit 0/1 pattern

--
