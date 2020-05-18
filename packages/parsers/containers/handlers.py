from collections import namedtuple
import re
from datetime import datetime


def add(name, property_name: str, tag: str, parents: list = None, regex=True):
    parents = parents or ['']
    tag = tag.lower()
    parents = [parent.lower() for parent in parents]
    container = namedtuple(name, ['property_name', 'tag', 'parents'])
    if regex:
        container.tag = re.compile(f'\w*{tag}\w*')
    else:
        container.tag = tag
    container.parents = parents
    container.property_name = property_name
    return container


class Handler:
    paths = ()
    __input_pattern_datetime = '%Y-%m-%dT%H:%M:%S'
    __output_pattern_datetime = '%F %T'

    def dict(self):
        return {path.__name__: self.__getattribute__(path.property_name) for path in self.paths}

    def handle_date(self, date):
        date = date[:19]
        date = datetime.strptime(date, self.__input_pattern_datetime)
        date = datetime.strftime(date, self.__output_pattern_datetime)
        return date
