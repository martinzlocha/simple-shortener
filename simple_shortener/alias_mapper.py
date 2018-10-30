import random
import string

from tinydb import Query

from simple_shortener import app


class AliasMapper:
    def __init__(self, db):
        self._db = db

    def _generate_string(self):
        possible_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '-_'
        return ''.join(random.choice(possible_chars) for _ in range(app.config['ALIAS_LENGTH']))

    def get_url(self, alias):
        result = self._db.search(Query().alias == alias)

        if not result:
            raise KeyError('No match for alias {} found.'.format(alias))
        elif len(result) > 1:
            raise KeyError('Multiple matches for alias {}. There should only be one result.'.format(alias))
        elif 'url' not in result[0] or 'alias' not in result[0]:
            raise ValueError('Each entry should contain an alias and a url.')
        else:
            return result[0]['url']

    def store_url(self, url):
        alias = self._generate_string()

        while self._db.contains(Query().alias == alias):
            alias = self._generate_string()

        self._db.insert({'alias': alias, 'url': url})

        return alias

