class Blog:
    def __init__(self,title,author,posts):
        self.title = title
        self.author= author
        self.posts = []

    def __repr__(self):
        return '{} by {} ({} post{})'.format(self.title,
                                           self.author,
                                           len(self.posts), 
                                           's' if len(self.post) != 1 else " ")


    def create_post(self,title,content):
        self.title = title
        self.content = content

    def json(self):
        return{
            "title": self.title,
            "content": self.content
        }



