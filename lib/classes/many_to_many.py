import ipdb; 
class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)#on init ,append every new instance to the list 
        

    @property
    def title(self):
        return self._title
    # @title.setter
    # def title(self,title):
    #     if not isinstance(title, str):
    #         raise TypeError("Title must be a string")
    #     if not (5 <= len(title) <= 50):
    #          raise ValueError("Title must be greater 5 and less that 50")
    #     self._title = title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise TypeError("Author must be an instance of Author")
    
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, magazine):
    
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise TypeError("Magazine must be an instance of Magazine")
        
       



class Author:
    def __init__(self, name):
        
    
        self._name = name
        self._articles = [] # stores all the article instances associated with this author.
        #meaning every author keeps track of their own articles separately.


    @property 
    def name(self):
        return self._name#no setter because --name cannot be changed
    
    @property
    def articles(self):#rerutn all articles 
        return self._articles #allows me to say author.articles() and get all the articles associated with that author
       #[article for article in Article.all if article.author == self]
      

    def magazines(self):#return unique list of magazines for which author has contributed 

        return list(set(article.magazine for article in self._articles))
        pass

    def add_article(self, magazine, title):#create and return a new article instance and associate it with this author and the provided magazine 
        article = Article(self,magazine,title)
        self._articles.append(article)
        return article
      

    def topic_areas(self):#return a unique list of strings with the categories of the magazines the author has contributed to 
        if not self._articles:
            return None
        else:
            return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self , name):
        if not isinstance(name,str):
            raise TypeError("Name must be a string")
        if not( 2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = name
    

    def articles(self):
        return [article for article in Article.all if article.magazine == self]#list of all the articles the magazine has published
        
        pass
    
    def contributors(self):
        return list(set(article.author for article in Article.all if article.magazine ==self))#unique list of authors who have written for this magazine
        

        pass

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self ]
        return titles if titles else None

    def contributing_authors(self):
        author_count = {}#Key will be the author and value will be the count
        contributors =[]
        for article in Article.all:
            if article.magazine == self:
                if article.author in author_count:
                    author_count[article.author] += 1
                else:
                    author_count[article.author] = 1
        for author, count in author_count.items():#.items() ives the key value pairs
            if count > 2:
                contributors.append(author)
        return contributors if contributors else None
            

                
                
                    
                
        