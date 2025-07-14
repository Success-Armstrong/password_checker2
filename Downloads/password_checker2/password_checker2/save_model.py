# save_model.py
import pickle
from sklearn.ensemble import RandomForestClassifier

# Dummy dataset: [length, has_digit, has_special, has_upper, has_lower]
X = [
    [5, 0, 0, 0, 1],  # Weak
    [10, 1, 0, 0, 1], # Medium
    [12, 1, 1, 1, 1], # Strong
    [7, 1, 0, 1, 1],  # Medium
]
y = ['Weak', 'Medium', 'Strong', 'Medium']

model = RandomForestClassifier()
model.fit(X, y)

with open('model/password_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved to model/password_model.pkl")
