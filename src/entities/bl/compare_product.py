import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

from src.entities.enum.brands import Brands


class CompareProduct:

    @staticmethod
    def compare(first_product: str, second_product: str) -> float:
        vector = CountVectorizer(stop_words=[*Brands.SHAMPOO_BRANDS.value])
        s = vector.fit_transform([first_product, second_product]).toarray()
