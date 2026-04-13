import pickle


def load() -> list:

    with open('data.pkl', 'rb') as f:
        loaded_data = pickle.load(f)

    return loaded_data