import string

def evaluate_password(password, model):
    # Extract features for ML model (length, digits, symbols, etc.)
    features = [
        len(password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password),
        any(c.isupper() for c in password),
        any(c.islower() for c in password)
    ]
    prediction = model.predict([features])[0]

    suggestions = []
    if len(password) < 8:
        suggestions.append("Use at least 8 characters")
    if not any(c.isdigit() for c in password):
        suggestions.append("Include numbers")
    if not any(c.isupper() for c in password):
        suggestions.append("Use uppercase letters")
    if not any(c in string.punctuation for c in password):
        suggestions.append("Add special characters")

    return prediction, suggestions
