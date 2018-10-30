import unittest

import simple_shortener


class Simple_shortenerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = simple_shortener.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to simple_shortener', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
