import os

from tinydb import TinyDB

import simple_shortener
from simple_shortener.alias_mapper import AliasMapper


class TestDatabase:
    def __init__(self):
        self._db_path = os.path.join('db', 'test.db')
        self.db = TinyDB(self._db_path)
        self.alias_mapper = AliasMapper(self.db)

    def inject_into_api(self):
        simple_shortener.api.alias_mapper = self.alias_mapper

    def __del__(self):
        self.db.close()
        os.remove(self._db_path)