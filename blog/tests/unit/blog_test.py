from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test", 'Test_author')
    

        self.assertEqual("Test", b.title)
        self.assertEqual('Test_author', b.author)
        self.assertListEqual([], b.posts)