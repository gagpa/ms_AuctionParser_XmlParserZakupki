from .interface.IContent import IContent as Interface

from bs4 import BeautifulSoup


class ContentLocal(Interface):

    def get_content(self, local_path: str) -> type(BeautifulSoup):
        """Получить bs object из xml"""
        with open(local_path, 'r') as f:
            return BeautifulSoup(f.read(), 'lxml')
