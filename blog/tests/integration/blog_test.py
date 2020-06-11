from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in blog(self):
        b = Blog("Test", 'Test_author')
        b.create_post('test post', 'test content')

        self.assertEqual(len(b.posts),1)
        self.assertEqual(b.post[0].title,'test post')
        self.assertEqual(b.post[0].content,'test content')

    def test_json_no_posts(self):
        b = Blog("Test", 'Test_author')
        excepted = {'title': 'Test', 'author':'Test Author', 'post':[]}

        self.assertDictEqual(excepted, b.json())


    def test_json(self):
        b = Blog("Test", 'Test_author')
        b.create_post('test post', 'test content')

        expected = {
            "title":"Test", 
            "author":'Test_author', 
            "posts":[
                { "title": 'test post',
                   "content": "test content"}]}

        self.assertDictEqual(expected, b.json())
