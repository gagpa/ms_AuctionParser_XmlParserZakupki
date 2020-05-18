from .configs import main_configs, ConfigID

from os import environ
from flask import Flask


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(main_configs[config_name])
    main_configs[config_name].init_app(app)
    from ms_app.api import api
    app.register_blueprint(api, url_prefix='/api/v1')
    return app


app = create_app(environ.get('APP_MODE') or 'development')
