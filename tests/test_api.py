import json
import unittest

import simple_shortener
from tests.test_database import TestDatabase


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = simple_shortener.app.test_client()
        self.database = TestDatabase()
        self.database.inject_into_api()

    def test_correct_response_code(self):
        response = self.app.post('/shorten_url', data={'url': 'https://google.com'})
        self.assertEqual(response.status_code, 201)

    def test_no_empty_url(self):
        response = self.app.post('/shorten_url', data={'url': ''})
        self.assertEqual(response.status_code, 400)

    def test_invalid_url(self):
        response = self.app.post('/shorten_url', data={'url': 'invalid-url'})
        self.assertEqual(response.status_code, 400)

    def test_disallow_javascript(self):
        response = self.app.post('/shorten_url', data={'url': 'javascript: (function(){})'})
        self.assertEqual(response.status_code, 400)

    def test_empty_post_fails(self):
        response = self.app.post('/shorten_url')
        self.assertEqual(response.status_code, 400)

    def test_invalid_alias(self):
        response = self.app.get('/test')
        self.assertEqual(response.status_code, 404)

    def test_valid_alias(self):
        target_url = 'https://google.com'
        response = self.app.post('/shorten_url', data={'url': target_url})
        data = json.loads(response.get_data(as_text=True))

        self.assertTrue('shortened_url' in data)

        response = self.app.get(data['shortened_url'])

        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.location, target_url)

    def tearDown(self):
        del self.database


if __name__ == '__main__':
    unittest.main()