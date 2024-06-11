import json


def read_vocab() -> list:
    with open("./static/vocab.json", "r") as file:
        vocab = json.load(file)
        return vocab


def read_index() -> list:
    with open("./static/index.json", "r") as file:
        index = json.load(file)
        return index
