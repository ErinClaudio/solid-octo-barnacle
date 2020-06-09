from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test content', p.content)

    def test_json(self):
        j = Post('Test', 'Test content')
        expected ={ 'title': 'Test','content': 'Test content' }

        self.assertDictEqual(expected,j.json())

