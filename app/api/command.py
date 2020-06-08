from flask import jsonify, request

from configs import ConfigDealer
from packages.package_dealer import PackageDealer
from . import api


@api.route('/parse_url')
def parse_xml():
    """Api команда. Передает объект Auction, Customer, Lots, полученные по ссылке urlXml."""
    xml_url = request.args.get('xml_url')
    if xml_url:
        parser_name = 'PARSER_XML_URL'

        parser = PackageDealer.get_parser(parser_name)()
        info = parser.parse(xml_url)
        if info:
            return jsonify({'status': True,
                            'data': info})

        return jsonify({'status': False,
                        'massage': f'Информация не найдена: {xml_url}'})

    return jsonify({'status': False,
                    'message': 'Ссылка не получена. Убедитесь что вы передали её в переменной'})


@api.route('/parse_name')
def parse_name():
    """
    Api команда. Передает тип файла, номер аукциона, внутренний номер(нужен для составления ссылки на XmlFile),
    полученные из названий файлов Xml.
    """
    local_path = request.args.get('local_path')
    if local_path:
        config_name = 'PARSER_XML_NAME'
        parser_name = 'PARSER_XML_NAME'

        config = ConfigDealer.get_package_config(config_name)
        parser = PackageDealer.get_parser(parser_name)(config)
        data = parser.parse(local_path)
        if data:
            return jsonify({'status': True,
                            'data': data})

        return jsonify({'status': False,
                        'massage': f'Файлы не найдены: {config.parse_path}'})

    return jsonify({'status': False,
                    'message': 'Параметр <link> не передан'})
