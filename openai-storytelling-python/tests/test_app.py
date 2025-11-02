import unittest
from openai_storytelling.main import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_story(self):
        response = self.app.post('/api/stories', json={
            'title': 'Test Story',
            'content': 'This is a test story.',
            'author': 'Author Name'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test Story', str(response.data))

    def test_get_stories(self):
        response = self.app.get('/api/stories')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

if __name__ == '__main__':
    unittest.main()