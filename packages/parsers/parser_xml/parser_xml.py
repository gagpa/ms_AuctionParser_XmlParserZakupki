from bs4 import BeautifulSoup


class ParserXml:
    """Парсер XmlFile"""

    @staticmethod
    def is_xml(file_name: str) -> bool:
        """Проверить ТипФайла"""
        return file_name.endswith('xml')

    def parse_xml(self, xml, container):
        for path in container.paths:
            value = self.find_tag(xml, path.tag, path.parents)
            if value:
                setattr(container, path.property_name, value)
        return container

    def find_tag(self, xml: BeautifulSoup, tag: str, parents: list = None):
        """Найти tag по parent в Xml"""
        info = []
        parents = parents or ['']
        for current_tag in xml.find_all(tag):
            for parent in parents:
                if parent in current_tag.parent.name:
                    info.append(current_tag.text)
                    break
        return info
