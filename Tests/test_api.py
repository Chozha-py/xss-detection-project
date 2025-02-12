import unittest
import requests

class TestXSSDetection(unittest.TestCase):
    BASE_URL = 'http://localhost:5000'

    def test_malicious_input(self):
        response = requests.post(f'{self.BASE_URL}/detect-xss', json={'input': "<script>alert('XSS')</script>"})
        self.assertEqual(response.json()['status'], 'malicious')

    def test_benign_input(self):
        response = requests.post(f'{self.BASE_URL}/detect-xss', json={'input': "Hello, world!"})
        self.assertEqual(response.json()['status'], 'benign')

if __name__ == '__main__':
    unittest.main()
