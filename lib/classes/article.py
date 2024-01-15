class Article:
    def __init__(self, author, magazine, title, word_count):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.word_count = word_count
        author.articles.append(self)
        magazine.articles.append(self)

    @property
    def word_count(self):
        return self._word_count
    
    @word_count.setter
    def word_count(self, word_count):
        if word_count > 0:
            self._word_count = word_count
        else:
            raise Exception("Word count cannot be less than 1")
        
    def __repr__(self) -> str:
        return f"<Article {self.title} - {self.author} - {self.magazine} - {self.word_count}"
