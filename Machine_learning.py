#Why this matters:
'''Machine Learning (ML) helps systems to learn from data and make decisions based on that data.
It powers everything from recommendation systems (like Netflix or Amazon) to self-driving cars.'''

#--------------------------------------------------------------------------------------------------

#Supervised Learning:
#Definition:
'''The model learns from labeled data (input-output pairs).'''
#Example:
'''If you have data with features like "hours studied" and the label "pass/fail,"
the model will learn to predict whether a student will pass based on the hours they studied.'''

#Types of Supervised Learning:
#Classification (predicting categories): 
'''Example – Spam email classification.'''
#Regression (predicting continuous values): 
'''Example – Predicting house prices.'''

#--------------------------------------------------------------------------------------------------

#Unsupervised Learning:
#Definition: 
'''The model tries to identify patterns or structures in unlabeled data.'''

#Example:
''' Grouping customers into segments based on their purchasing behavior without knowing their exact categories beforehand.'''

#Types of Unsupervised Learning:
#Clustering (grouping similar data):
'''Example – Segmenting customers into different groups based on spending habits.'''
#Dimensionality Reduction (reducing the number of features while preserving data characteristics):
'''Example – Reducing the complexity of an image while retaining important features.'''

#--------------------------------------------------------------------------------------------------

#🔍 Examples:
# Predicting the price of a used car based on its model, mileage, and year.
'''✅ It is Supervised Learning – because we have labeled data: input features (model, mileage, year) and output label (car price).
✅ It’s Regression, because the output (price) is a continuous numerical value — not a category like "yes" or "no."
'''

# Grouping customers into segments based on their shopping behavior.
'''✅ This is Unsupervised Learning – because there are no predefined labels (we don’t tell the model what the segments are).
✅ The goal is to discover patterns or groups in the data.
✅ And yes, this is a perfect use case for Clustering.
'''

# Detecting whether a transaction is fraudulent or not.
'''✅ Supervised Learning – because we have labeled data: past transactions labeled as "fraud" or "not fraud".
✅ It’s a Classification problem – the output is categorical (fraudulent or not).
'''

# Forecasting the temperature for the next week.
'''✅ Supervised Learning – historical temperature data (input) with known future temperatures (labels).
✅ It’s a Regression task – because the temperature is a continuous numerical value (e.g., 28.5°C).
'''

# Recommending movies to users based on their viewing history.
'''This usually falls under Reinforcement Learning or Supervised Learning (when feedback like ratings is available), 
but in many basic recommender systems, especially collaborative filtering, it works like:
👉 Unsupervised Learning – but not necessarily Clustering
It’s more about pattern matching and similarity detection (e.g., finding similar users or similar movies),
not always about forming distinct clusters.
So:
✅ Often considered Unsupervised, especially in unsupervised collaborative filtering methods.
'''

# Recognizing whether an email is spam or not.
'''✅ Supervised Learning – You train the model with emails labeled as "spam" or "not spam."
✅ It’s Classification – because the goal is to assign the email to one of two categories.
'''

# Clustering similar news articles together.
'''✅ Unsupervised Learning – because the articles aren’t labeled by topic.
✅ It’s a classic case of Clustering – grouping similar content based on words, topics, or structure.
'''

# Predicting a patient’s blood sugar level based on medical history.
'''✅ Supervised Learning – because we have past medical data and actual blood sugar readings (labels).
✅ It’s Regression – because blood sugar level is a continuous value (e.g., 110 mg/dL, 145 mg/dL).
'''

# Grouping products that are often bought together.
'''✅ This is Unsupervised Learning — no labeled outputs, just patterns in data.
❌ But not exactly Clustering in the traditional sense.
🔍 Explanation: This problem is usually handled by Association Rule Learning, a type of unsupervised learning. 
It’s about finding relationships or rules like:
“If a person buys bread and butter, they often also buy jam.”
🧠 Algorithms used: Apriori, FP-Growth, etc.
'''

# Predicting if a person has diabetes (yes/no) based on age, weight, and insulin level.
'''✅ Supervised Learning – you have labeled data where each person is labeled with "yes" or "no" (has diabetes or not).
✅ It’s Classification – because you're predicting a category (yes or no).
'''
