from .content_makers.unpacker import Unpacker
from os import listdir, path
import re


class ParserName(Unpacker):

    """
    ParserID рассчитан на парсинг файлов скаченных с Ftp.
    Умеет:
     1) возвращать ссылки на XmlFiles из файлов скаченных с Ftp,
     2) распаковывать ZipFiles

    Возможные ошибки:
     1) названия файлов поменялось, поэтому метод __detect_prefix не срабатывает(проверить регулярное выражение
                                                                                 указанное в этом методе).
    """

    parse_path = None

    def __init__(self, config):
        """
        Config - это Python объект.
        Должен иметь свойства: 1) base_link - Базис ссылки на XmlFile;
                               2) save_path - локальный путь на директорию, куда объект может распаковывать файлы;
                               3) parse_path - путь который нужно будет обрабатывать.
        Директории ,на которые указаны пути, должны быть пустыми
        """
        self.save_path = config.save_path

    def parse(self, file_path=None) -> list:
        """
        Получает на вход путь(file_path) из которго нужно вытащить ссылки на XmlFiles.
        file_path: может быть XmlFile, ZipFile или директорией,
        На выход возвразается список из ссылок на XmlFiles
        """
        file_path = file_path or self.parse_path
        xml_paths = self.__get_xml_paths(file_path)
        if xml_paths:
            return list(map(self.__detect_prefix, xml_paths))

    def __get_xml_paths(self, files_path: str) -> list:
        """Выдает список ссылок на Xml_files, находящиеся по заданному пути(files_path)"""
        if self.is_dir(files_path):
            xml_paths = self.__xml_from_dir(files_path)
        elif self.is_pucked(files_path):
            xml_paths = self.__xml_from_zip(files_path)
        elif self.is_xml(files_path):
            xml_paths = [files_path]
        else:
            xml_paths = []
        return xml_paths

    def __xml_from_zip(self, zip_path: str) -> list:
        """Выдает все пути на XmlFiles, находящиеся в Zip архиве(zip_path)"""
        zip_name = zip_path.split('/')[-1]
        dir_name = zip_name.replace('.zip', '')
        save_path = '/'.join((self.save_path, dir_name))
        self.unpack(zip_path, save_path)
        file_paths = ['/'.join((save_path, name)) for name in listdir(save_path)]
        xml_paths = list(filter(self.is_xml, file_paths))
        dir_paths = list(filter(self.is_dir, file_paths))
        if dir_paths:
            for dir_path in dir_paths:
                xml_paths.extend(self.__xml_from_dir(dir_path))
        return xml_paths

    def __xml_from_dir(self, dir_path: str) -> list:
        """Выдаёт все пути на XmlFiles, находящиеся в директории(dir_path)"""
        file_paths = ['/'.join((dir_path, name)) for name in listdir(dir_path)]
        zips_paths = list(filter(self.is_pucked, file_paths))
        xml_paths = list(filter(self.is_xml, file_paths))
        dir_paths = list(filter(self.is_dir, file_paths))
        if dir_paths:
            for dir_path in dir_paths:
                xml_paths.extend(self.__xml_from_dir(dir_path))
        if zips_paths:
            for zip_path in zips_paths:
                xml_paths.extend(self.__xml_from_zip(zip_path))
        return xml_paths

    @staticmethod
    def is_xml(xml_path: str) -> bool:
        """Показывает является файл Xml"""
        return xml_path.endswith('.xml') and not ParserName.is_dir(xml_path)

    @staticmethod
    def is_dir(dir_path: str) -> bool:
        """Показывает является файл директорий или нет"""
        return path.isdir(dir_path)

    def __detect_prefix(self, xml_path: str) -> dict:
        """
        xml_path: локальный путь или название XmlFile.
        Извлекает из названия файла все его части
        1ая группа: тип файла,
        2ая группа: номер аукциона,
        3ая группа: внутренний номер(нужен для составления ссылки на XmlFile)
        """
        xml_name = xml_path.split('/')[-1]
        searched = re.match(r'([\w]*)(_[0-9]+)(_[0-9]+).xml', xml_name)
        if searched:
            type_name = searched.group(1)
            purchase_number = searched.group(2).replace('_', '')
            notice_id = searched.group(3).replace('_', '')
            return {'typeName': type_name,
                    'purchaseNumber': purchase_number,
                    'noticeId': notice_id}
