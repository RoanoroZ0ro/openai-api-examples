class Story:
    def __init__(self, title: str, content: str, author: str):
        self.title = title
        self.content = content
        self.author = author

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "author": self.author
        }