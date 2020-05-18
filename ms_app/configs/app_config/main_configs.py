import os


# basedir = os.path.abspath('.')


class Config:
    pass

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    PORT = '8081'
    IP = '0.0.0.0'
    DEBUG = True


class ProductionConfig(Config):
    pass


main_configs = {'default': DevelopmentConfig,
                'development': DevelopmentConfig,
                'production': ProductionConfig}
