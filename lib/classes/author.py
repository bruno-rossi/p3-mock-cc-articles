# from magazine import Magazine
# from article import Article

class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []
        self.magazines = []
        
    @property
    def name(self):
        """The name property"""
        return self._name
    
    @name.setter
    def name(self, name):
        """The name setter"""
        # print(type(name))
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        elif len(name) == 0:
            raise ValueError("Name must contain at least one letter")
        else:
            raise ValueError("Name must be a string")

    def get_magazines(self):
        for article in self.articles:
            if article.magazine in self.magazines:
                pass
            else:
                self.magazines.append(article.magazine)
        return self.magazines

    def has_written_for_magazine(self, magazine):
        self.get_magazines()
        if magazine in self.magazines:
            return True
        else:
            return False
        
    def __repr__(self) -> str:
        return f"<Author {self.name}"
        
# if __name__ == "__main__":
#     anne = Author('Anne')
#     mary = Author('Mary')
#     cosmo = Magazine('Cosmo', 'fashion')
#     vogue = Magazine('Vogue', 'fashion')
#     Article(anne, cosmo, '2023 Tennis Outfits', 250)
#     Article(mary, cosmo, '2024 and Beyond', 300)
#     Article(anne, cosmo, 'Annes tips', 200)
#     # print(cosmo.articles)
#     print(cosmo.get_top_contributor())