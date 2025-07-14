import pickle

def load_model():
    with open('model/password_model.pkl', 'rb') as f:
        return pickle.load(f)
