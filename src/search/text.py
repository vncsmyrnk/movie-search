import nltk
import string
from unidecode import unidecode
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


nltk.download("punkt")
nltk.download("stopwords")


def preprocess_text(texto: str) -> str:
    """
    Realiza operacoes de analise lexica em textos
    """
    stop_words = set(stopwords.words("english"))
    stemmer = PorterStemmer()

    # Remover acentos
    text = unidecode(texto)
    # Transforma o texto em minusculo
    text = text.lower()
    # Remover pontuação
    text = texto.translate(str.maketrans("", "", string.punctuation))
    # Análise Léxica
    tokens = word_tokenize(text)
    # Remoção de Stopwords
    tokens_sem_stopwords = [
        word for word in tokens if word.lower() not in stop_words
    ]
    # Stemming
    tokens_stemmed = [stemmer.stem(word) for word in tokens_sem_stopwords]
    return " ".join(tokens_stemmed)
