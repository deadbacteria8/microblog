"""
Factory for application
"""

import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask.logging import default_handler
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics
from honeybadger.contrib import FlaskHoneybadger
from honeybadger.contrib.logger import HoneybadgerHandler
from app.config import ProdConfig, RequestFormatter


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
bootstrap = Bootstrap()
moment = Moment()
#'hbp_s4S4BoIAyqht3QpwD8ikDuHBku60Z90a6xY7'

def create_app(config_class=ProdConfig):
    """
    Create flask app, init addons, blueprints and setup logging
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    if os.environ.get('FLASK_ENV', 'development') == "production":
        metrics = GunicornInternalPrometheusMetrics.for_app_factory()
        metrics.init_app(app)
    app.config['HONEYBADGER_ENVIRONMENT'] = 'production'
    app.config['HONEYBADGER_API_KEY'] = os.environ.get('HONEYBADGER')
    app.config['HONEYBADGER_PARAMS_FILTERS'] = 'password, secret, credit-card'
    FlaskHoneybadger(app, report_exceptions=True)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)
    

    #pylint: disable=wrong-import-position, cyclic-import, import-outside-toplevel
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    #pylint: enable=wrong-import-position, cyclic-import, import-outside-toplevel


    if not app.debug and not app.testing:
        formatter = RequestFormatter(
            '[%(asctime)s %(levelname)s] %(remote_addr)s requested %(url)s\n: %(message)s [in %(module)s:%(lineno)d]'
        )
        default_handler.setFormatter(formatter)
        app.logger.setLevel(logging.INFO)
        hb_handler = HoneybadgerHandler(api_key=app.config['HONEYBADGER_API_KEY'])
        app.logger.addHandler(hb_handler)

    return app


from app import models #pylint: disable=wrong-import-position, cyclic-import, import-outside-toplevel
