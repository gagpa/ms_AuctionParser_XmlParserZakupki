from packages.parsers import ParserName, ParserXmlZakupki44


class PackageDealer:

    __parsers = {'parser_name': ParserName,
               'parser_xml44': ParserXmlZakupki44}

    @classmethod
    def get_parsers(cls, parser_name):
        try:
            parser = cls.__parsers[parser_name]
            return parser
        except KeyError:
            print(f'Ваш ключ: {parser_name} не подходит. Возможные ключи: {cls.__parsers.keys()}')
            raise KeyError
