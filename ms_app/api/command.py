from . import api
from ms_app import ConfigID

from parsers.parser_xml import ParserXmlZakupki44
from parsers.parser_names import ParserID
from flask import jsonify, request


@api.route('/xml_url')
def parse_xml_url():
    """Api команда. Передает объект Auction, Customer, Lots, полученные по ссылке urlXml."""
    link = request.args.get('link')
    link = ''
    if link:
        parser = ParserXmlZakupki44()
        info = parser.parse(link)
        if info:
            return jsonify({'status': True,
                            'data': info})
        return jsonify({'status': False,
                        'massage': f'Информация не найдена: {link}'})
    return jsonify({'status': False,
                    'message': 'Ссылка не получена. Убедитесь что вы передали её в переменной'})


@api.route('/xml_local')
def parse_xml_local():
    """
    Api команда. Передает тип файла, номер аукциона, внутренний номер(нужен для составления ссылки на XmlFile),
    полученные из названий файлов Xml.
    """
    link = request.args.get('link')
    config = ConfigID
    parser = ParserID(config)
    data = parser.parse(link)
    if data:
        return jsonify({'status': True,
                        'data': data})
    return jsonify({'status': False,
                    'massage': f'Файлы не найдены: {ConfigID.parse_path}'})
