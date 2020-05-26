from . import api
from configs import ConfigDealer
from packages.package_dealer import PackageDealer

from flask import jsonify, request


@api.route('/xml')
def parse_xml():
    """Api команда. Передает объект Auction, Customer, Lots, полученные по ссылке urlXml."""
    link = request.args.get('link')
    parser_name = 'parser_xml44'
    if link:
        parser = PackageDealer.get_parsers(parser_name)()
        info = parser.parse(link)
        if info:
            return jsonify({'status': True,
                            'data': info})
        return jsonify({'status': False,
                        'massage': f'Информация не найдена: {link}'})
    return jsonify({'status': False,
                    'message': 'Ссылка не получена. Убедитесь что вы передали её в переменной'})


@api.route('/parser_name')
def parse_name():
    """
    Api команда. Передает тип файла, номер аукциона, внутренний номер(нужен для составления ссылки на XmlFile),
    полученные из названий файлов Xml.
    """
    link = request.args.get('link')
    config_name = 'parser_name'
    parser_name = 'parser_name'
    config = ConfigDealer.get_package(config_name)
    parser = PackageDealer.get_parsers(parser_name)(config)
    data = parser.parse(link)
    if data:
        return jsonify({'status': True,
                        'data': data})
    return jsonify({'status': False,
                    'massage': f'Файлы не найдены: {config.parse_path}'})
