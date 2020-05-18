from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


class IContent(ABC):

    @abstractmethod
    def get_content(self, path: str) -> BeautifulSoup:
        pass
