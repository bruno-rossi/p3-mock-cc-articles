class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must have at least one letter")

    def get_authors(self):
        authors = []
        for article in self.articles:
            if article.author in authors:
                pass
            else:
                authors.append(article.author)
        return authors

    def get_article_titles(self):
        article_titles = []
        for article in self.articles:
            article_titles.append(article.title)
        return article_titles

    def get_longest_article(self):
        longest_article = None
        for article in self.articles:
            if longest_article == None:
                longest_article = article
            elif article.word_count > longest_article.word_count:
                longest_article = article
        return longest_article

    def get_average_word_count(self):
    
        lengths = []
        for article in self.articles:
            lengths.append(article.word_count)
        return sum(lengths) / len(self.articles)
    
    def get_top_contributor(self):
        """Note this method is an optional stretch goal"""
        
        authors = {}
        for article in self.articles:
            if article.author in authors:
                authors.update({article.author: authors.get(article.author) + 1})
            else: 
                authors.update({article.author: 1})

        # print(authors)

        top_contributor = None 
        for author in authors:
            if top_contributor == None:
                top_contributor = author
            elif authors.get(author) > (authors.get(top_contributor)):
                top_contributor = author

        return top_contributor

    def __repr__(self) -> str:
        return f"<Magazine {self.name}"
