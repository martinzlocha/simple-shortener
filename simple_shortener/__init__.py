import os

from flask import Flask
from flask_caching import Cache
from tinydb import TinyDB

app = Flask(__name__)
app.config.from_object('simple_shortener.default_settings')
app.config.from_envvar('SIMPLE_SHORTENER_SETTINGS')

db = TinyDB(os.path.join('db', 'store.db'))

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

if not app.debug:
    import logging
    from logging.handlers import TimedRotatingFileHandler
    # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
    file_handler = TimedRotatingFileHandler(os.path.join(app.config['LOG_DIR'], 'simple_shortener.log'), 'midnight')
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter('<%(asctime)s> <%(levelname)s> %(message)s'))
    app.logger.addHandler(file_handler)


import simple_shortener.api
