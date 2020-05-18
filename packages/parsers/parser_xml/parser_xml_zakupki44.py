from .parser_xml import ParserXml
from .content_makers.url import ContentUrl
from ..containers import ContainerFactory

from bs4 import BeautifulSoup


class ParserXmlZakupki44(ParserXml, ContentUrl):
    """Парсер XmlFile по URL"""
    paths = {}

    def parse(self, url_path) -> dict:
        xml = self.get_content(url_path)
        customers = self.parse_customers(xml)
        lots = self.parse_lots(xml)
        auction = self.parse_auction(xml)
        if auction and customers and lots:
            parse_info = {
                'auction': auction.dict(),
                'customers': {'totalItems': len(customers),
                              'items': [customer.dict() for customer in customers]},
                'lots': {'totalMaxPrice': sum([lot.max_price for lot in lots if lot.max_price]),
                         'totalItems': len(lots),
                         'items': [lot.dict() for lot in lots]}
                         }
            return parse_info

    def parse_lots(self, xml: BeautifulSoup) -> list:
        """Парсит Xml объект.
        return: list(lot, ...)
        """
        main_tags = ContainerFactory.get_container('lot').main_tags
        for main_tag in main_tags:
            xmls = xml.find_all(main_tag)
            if xmls:
                lots_dicts = []
                for xml in xmls:
                    lot_dict = self.parse_xml(xml, ContainerFactory.get_container('lot'))
                    lots_dicts.append(lot_dict)
                return lots_dicts

    def parse_customers(self, xml: BeautifulSoup) -> list:
        """
        Парсит Xml объект.
        return: list(customer, ...)
        """
        main_tags = ContainerFactory.get_container('customer').main_tags
        for main_tag in main_tags:
            xmls = xml.find_all(main_tag)
            if xmls:
                customers_dicts = []
                for xml in xmls:
                    customer_dict = self.parse_xml(xml, ContainerFactory.get_container('customer'))
                    customers_dicts.append(customer_dict)
                return customers_dicts

    def parse_auction(self, xml: BeautifulSoup) -> dict:
        """
        Парсит Xml объект.
        return: list(auction, ...)
        """
        auction = self.parse_xml(xml, ContainerFactory.get_container('auction'))
        return auction
