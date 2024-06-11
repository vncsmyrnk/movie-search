import json


def read_vocab() -> list:
    """Reads and returns the contents of vocab as json"""
    with open("./static/vocab.json", "r") as file:
        vocab = json.load(file)
        return vocab


def read_index() -> list:
    """Reads and returns the contents of index as json"""
    with open("./static/index.json", "r") as file:
        index = json.load(file)
        return index


def read_reviews() -> list:
    """Reads and returns the contents of reviews as json"""
    with open("./static/reviews_processed.json", "r") as file:
        index = json.load(file)
        return index
