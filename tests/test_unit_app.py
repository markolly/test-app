import unittest
from unittest.mock import patch
from app import hello

class AppTestCase(unittest.TestCase):
    @patch('app.render_template')  # Mock the render_template function
    def test_hello(self, mock_render_template):
        # Set up the mock render_template function to return a specific value
        mock_render_template.return_value = "<h1>Hello App</h1>"

        result = hello()

        self.assertEqual(result, "<h1>Hello App</h1>")
        mock_render_template.assert_called_with('index.html')

if __name__ == '__main__':
    unittest.main()
