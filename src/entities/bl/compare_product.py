import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

from src.entities.enum.brands import Brands


class CompareProduct:

    @staticmethod
    def compare(first_product: str, second_product: str) -> float:
        vector = CountVectorizer(stop_words=[*Brands.SHAMPOO_BRANDS.value])
        s = vector.fit_transform([first_product, second_product]).toarray()
        return 1 - (np.linalg.norm(s[0] - s[1]) /
                    np.linalg.norm(np.array([0 for i in range(len(vector.vocabulary_))]) -
                                   np.array([1 for i in range(len(vector.vocabulary_))])))
