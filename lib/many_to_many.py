class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        related_contracts = self.contracts()
        related_books = []
        for related_contract in related_contracts:
            related_books.append(related_contract.book)
        return related_books
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        related_contracts = self.contracts()
        total_royalties = 0
        for related_contract in related_contracts:
            total_royalties += related_contract.royalties
        return total_royalties

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        related_contracts = self.contracts()
        related_authors = []
        for related_contract in related_contracts:
            related_authors.append(related_contract.author)
        return related_authors
    


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Needs to be type Author")
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception("book needs to be Book")
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if (isinstance(date, str)):
            self._date = date
        else:
            raise Exception("date must be a string")
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception("royalties musy be an integer")
    
    def contracts_by_date(self):
        for x in Contract.all:
            print(x.date)
        sorted_date = sorted(Contract.all, key=lambda contract: contract.date)
        for x in sorted_date:
            print(x.date)
        return sorted_date