# AINurse - Simple Health Classification Demo
# Copyright © 2025 Sara Ghalib Al-Harbi – All Rights Reserved

from sklearn.tree import DecisionTreeClassifier

# Sample data: [heart rate, body temperature]
X = [
    [80, 37],
    [120, 39],
    [90, 36.5],
    [110, 38.2],
    [70, 36.9]
]
y = ['Stable', 'Critical', 'Stable', 'Critical', 'Stable']

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict the condition of a sample patient
sample = [[100, 38]]
result = model.predict(sample)

print("Patient condition:", result[0])
