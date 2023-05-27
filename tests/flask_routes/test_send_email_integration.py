import unittest
import requests
import json

class EmailTestCase(unittest.TestCase):
    def setUp(self):
        # Define the URL of your Flask application
        self.url = 'http://localhost:8888/send_email'

        # Define the JSON payload for the POST request
        self.payload = {
            'name': 'John',
            'surname': 'Doe',
            'phone': '123456789',
            'email': 'john.doe@example.com',
            'topic': 'Test Email',
            'text': 'This is a test email message.'
        }

        # Convert the payload to JSON format
        self.json_payload = json.dumps(self.payload)

        # Set the Content-Type header to specify JSON data
        self.headers = {'Content-Type': 'application/json'}

    def test_send_email(self):
        # Send the POST request
        response = requests.post(self.url, data=self.json_payload, headers=self.headers)

        # Check the response status code
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Email sent successfully')

if __name__ == '__main__':
    unittest.main()