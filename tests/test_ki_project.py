from flask import Flask
import os
import ki_project
import unittest

app = Flask(__name__)


class KiProjectTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')
        # assert the response data
        self.assertTrue(result.data, bytearray)

if __name__ == '__main__':
    unittest.main()
