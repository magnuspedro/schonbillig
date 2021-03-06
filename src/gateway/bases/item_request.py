from abc import ABCMeta, abstractmethod


class ItemRequest(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_next_url') and
                callable(subclass.get_next_url) and
                hasattr(subclass, 'get_list_url') and
                callable(subclass.get_list_url) and
                hasattr(subclass, 'request_itens') and
                callable(subclass.request_items) or
                NotImplemented)

    @abstractmethod
    def get_next_url(self, page_source: str) -> str:
        """
        Return "Add to watch list" button url.
        """
        raise NotImplementedError

    @abstractmethod
    def get_list_url(self, page_source: str) -> list:
        """
        Return "Add to watch list" button url.
        """
        raise NotImplementedError

    @abstractmethod
    def request_items(self) -> list:
        """
        Request page intens and return.
        """
        raise NotImplementedError
