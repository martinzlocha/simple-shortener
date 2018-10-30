import unittest

import simple_shortener


class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = simple_shortener.app.test_client()

    def test_correct_response_code(self):
        response = self.app.post('/shorten_url', data={'url': 'google.com'})
        self.assertEqual(response.status_code, 201)

    def test_get_is_invalid(self):
        response = self.app.get('/shorten_url')
        self.assertEqual(response.status_code, 405)

    def test_empty_post_fails(self):
        response = self.app.post('/shorten_url')
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
