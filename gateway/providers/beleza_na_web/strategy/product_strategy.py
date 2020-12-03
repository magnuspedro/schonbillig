from abc import ABCMeta, abstractmethod


class ProductStrategy(metaclass=ABCMeta):
    @abstractmethod
    def choose_product(self) -> str:
        raise NotImplementedError
