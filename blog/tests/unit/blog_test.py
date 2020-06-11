from unittest import TestCase
from blog import Blog

#test


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test", 'Test_author')
    

        self.assertEqual("Test", b.title)
        self.assertEqual('Test_author', b.author)
        self.assertListEqual([], b.posts)
    
    def test_repr(self):
        b = Blog("Test", 'Test_author')
        b2 = Blog('My Day', 'Rolf')

        self.assertEqual(b.__repr__(), 'Test by Test Author(0 posts)')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf(0 posts)')
    
    def test_repr_multiple_posts(self):
        b = Blog("Test", 'Test_author')
        b.posts= ['test']
        b2 = Blog('My Day', 'Rolf')
        b2.posts = ['test', 'another']

        self.assertEqual(b.__repr__(), 'Test by Test Author(0 posts)')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf(2 posts)')

    def test_create_post_in_blog(self):
        b = Blog("Test", 'Test_author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.create_post[0].title, 'Test Post')
        self.assertEqual(b.create_post[0].Content,'Test Content')


      

