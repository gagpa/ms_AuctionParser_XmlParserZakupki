from os import environ


class ConfigParserName:
    """
    Конфиг для ParserName, который парсит только названия файлов
    в {save_path} положить путь с директорией в которую нужно распаковать файлы ZIP
    """

    save_path = environ.get('UNPACK_PATH')
