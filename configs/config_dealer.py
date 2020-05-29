from configs.package_configs import package_configs
from configs.app_configs import main_configs


class ConfigDealer:

    __main = main_configs
    __packages = package_configs

    @classmethod
    def get_main(cls, config_name):
        try:
            config = cls.__main[config_name]
            return config()
        except KeyError:
            print(f'Ваш ключ: {config_name} не подходит. Возможные ключи: {cls.__main.keys()}')
            raise KeyError

    @classmethod
    def get_package_config(cls, package_name):
        try:
            config = cls.__packages[package_name]
            return config()
        except KeyError:
            print(f'Ваш ключ: {package_name} не подходит. Возможные ключи: {cls.__packages.keys()}')
            raise KeyError
