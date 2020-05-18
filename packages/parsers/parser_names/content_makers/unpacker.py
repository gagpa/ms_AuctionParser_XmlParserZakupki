from zipfile import ZipFile, BadZipFile, is_zipfile
from os import stat


class Unpacker:
    """Класс распаковищика файлов"""
    count_unpacked = 0

    def unpack(self, file_path: str, save_path: str):
        """Разархивировать"""
        if self.is_pucked(file_path):
            with ZipFile(file_path, 'r') as file:
                file.extractall(save_path)
                self.count_unpacked += 1
            return True
        else:
            raise BadZipFile()

    @staticmethod
    def is_pucked(file_path: str) -> bool:
        """Првоерить запакован файл или нет"""
        return is_zipfile(file_path) and stat(file_path).st_size > 22
