from .interface.IContent import IContent as Interface

from bs4 import BeautifulSoup
import requests


class ContentUrl(Interface):

    _headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

    def get_content(self, link: str):
        try:
            response = requests.get(link, headers=self._headers)
            if response.status_code != 200:
                raise ConnectionError
            html = response.content
            return BeautifulSoup(html, 'html.parser')
        except ConnectionError:
            return None
        except requests.exceptions.MissingSchema:
            return None
