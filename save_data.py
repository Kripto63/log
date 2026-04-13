import pickle


def save(data):
    with open('data.pkl', 'wb') as f:
        pickle.dump(data, f)