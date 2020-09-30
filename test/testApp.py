import sys,os
sys.path.append(os.getcwd())

from app import app
import os
import unittest

class AppTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def testCheck(self):
        response = self.app.get('/api/status')
        self.assertEqual(response.data, b'Up and Running ! :)')

if __name__ == '__main__':
    unittest.main()
