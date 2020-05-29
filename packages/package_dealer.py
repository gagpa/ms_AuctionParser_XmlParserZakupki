from packages.parsers import parsers


class PackageDealer:

    __parsers = parsers

    @classmethod
    def get_parser(cls, parser_name):
        try:
            parser = cls.__parsers[parser_name]
            return parser
        except KeyError:
            print(f'Ваш ключ: {parser_name} не подходит. Возможные ключи: {cls.__parsers.keys()}')
            raise KeyError
