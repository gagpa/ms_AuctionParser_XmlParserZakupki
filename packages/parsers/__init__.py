from .parser_xml.parser_xml_zakupki44 import ParserXmlZakupki44
from .parser_names.parser_id import ParserID


def test_run():
    links = ['https://zakupki.gov.ru/epz/order/notice/printForm/viewXml.html?noticeId=1966786']
    info = []
    parser = ParserXmlZakupki44()
    for link in links:
        info.append(parser.parse(link))
    return info
