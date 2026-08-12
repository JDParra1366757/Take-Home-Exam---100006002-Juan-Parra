class Book: 

    def __init__(self, title, author, year):
        self.title = title 
        self.author = author
        self.year = int(year)

    def __str__ (self): 
        return f"{self.title} by {self.author} ({self.year})"

    def __repr__ (self): 
        return f"Title = {self.title}, Author = {self.author}, Year = {self.year}"

    def __eq__(self,other):
        self.title == other.title
        self.author == other.author

    def age (self):
        self.yearint = int(self.year)
        age = 2026 - self.yearint
        print (f"{self.title} is {age} years old.")

class EBook:

    def __init__(self, title, author, year, sizemb):
        Book.__init__(self, title, author, year)
        self.sizemb = int(sizemb)

    def __str__ (self): 
        return f"{self.title} by {self.author} ({self.year})(Size: {self.sizemb}mb)"

    def __repr__ (self): 
        return f"Title = {self.title}, Author = {self.author}, Year = {self.year}, Size in Megabytes: {self.sizemb}"

    def download_seconds(self,mbitpsecs):
        self.mbps = mbitpsecs
        dlspeed = self.sizemb/self.mbps
        print(f"{self.title} will be downloaded in {dlspeed:.3} seconds.")

    def age (self):
        self.yearint = int(self.year)
        age = 2026 - self.yearint
        print (f"{self.title} is {age} years old.")

class Library:
        
    def __init__(self):
        self.collection = []

    def __repr__(self):
        return f"The Library has the following books: \n{self.collection}"

    def __len__(self):
        print(f"There are {len(self.collection)} book(s) in the library.")
        return len(self.collection)

    def add(self,book):
        loopy = 0

        for x in self.collection:
            if book.title == x.title:
                return print(f"{x.title} is already in the collection.")
            else:
                loopy += 1

        if loopy == len(self.collection):
            self.collection.append(book)
        else:
            pass

    def find_by_author(self, author):
        x = 0 
        z = 0

        print(f"The books written by {author} are:")
        for x in self.collection:
            if author == x.author:
                print(f"- {x.title}")
                z += 1

        if z == 0:
            print("- None")
        else:
            pass

    def oldest(self):
        oldy = 0
        tempage = 9999

        for x in self.collection:
            if x.year < tempage:
                tempage = x.year
                oldy = x.title
            else:
                pass

        print(f"The oldest book is {oldy}")




MunicipalLibrary = Library()
book1 = Book("House of Leaves","Mark Z. Danielewski","2001")
book2 = Book("Beastars Vol. 1","Paru Itagaki","2017")
book3 = Book("Beastars Vol. 15","Paru Itagaki","2019")
book4 = Book("The Hound of the Baskervilles","Arthur Conan Doyle","1902")
book5 = Book("House of Leaves","Mark Z. Danielewski","2001")
ebook1 = EBook("Dorohedoro - Volume 1","Q Hayashida","2000","250")
ebook2 = EBook("The Jojolands - Volume 1","Hirohiko Araki","2023","300")
ebook3 = EBook("There is no antimemetics division","QNTM","2020","450")
MunicipalLibrary.add(book1)
MunicipalLibrary.add(book2)
MunicipalLibrary.add(book3)
MunicipalLibrary.add(book4)
MunicipalLibrary.add(book5) #repeat book
MunicipalLibrary.add(ebook1)
MunicipalLibrary.add(ebook2)
MunicipalLibrary.add(ebook3)
print(book2)
print(ebook1)
book4.age()
ebook2.download_seconds(11)
MunicipalLibrary.find_by_author("Paru Itagaki")
MunicipalLibrary.oldest()
len(MunicipalLibrary)