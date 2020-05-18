from os import environ


class ConfigID:
    """
    Конфиг для Parser_id, Который парсит только названия файлов
    в {save_path} положить путь с директорией в которую нужно распаковать файлы ZIP
    в {parse_path} положить путь до файлов которую нужно запарсить
    """

    save_path = environ.get('UNPACK_PATH')
    parse_path = environ.get('DEFAULT_LOCAL_PARSE_PATH')
