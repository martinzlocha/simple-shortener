import random
import unittest

import simple_shortener
from tests.test_database import TestDatabase


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = simple_shortener.app.test_client()
        self.database = TestDatabase()
        self.alias_mapper = self.database.alias_mapper

    def test_two_keys_are_not_same(self):
        random.seed(0)
        alias1 = self.alias_mapper.store_url('')

        random.seed(0)
        alias2 = self.alias_mapper.store_url('')

        self.assertNotEqual(alias1, alias2)

    def test_can_retrieve_correctly(self):
        url = 'test'
        alias = self.alias_mapper.store_url(url)
        retrieved_url = self.alias_mapper.get_url(alias)

        self.assertEqual(url, retrieved_url)

    def test_raise_exception_if_url_doesnt_exist(self):
        with self.assertRaises(KeyError):
            self.alias_mapper.get_url('')

    def tearDown(self):
        del self.database


if __name__ == '__main__':
    unittest.main()
