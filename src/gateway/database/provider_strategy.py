from abc import ABCMeta, abstractmethod


class ProviderStrategy(metaclass=ABCMeta):
    @abstractmethod
    def choose_provider(self):
        raise NotImplementedError
