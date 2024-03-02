class libEditCatalog:
    def addBook(self, book, lib):
        print("Not implemented")
        pass
    def removeBook(self, book, lib):
        print("Not implemented")
        pass

class libSearch:
    def searchBook(self, book, lib):
        print("Not implemented")
        pass

class libBorrow:
    def borrowBook(self, book, lib):
        print("Not implemented")
        pass
    def returnBook(self, book):
        print("Not implemented")
        pass

class libReport:
    def generateReport():
        print("Not implemented")
        pass

class Guest(libSearch):
    def searchBook(self, book, lib):
        for item in lib:
            if book == item:
                print("Item found")
                return True
        return False 


class User(libBorrow, libSearch):
    def __init__(self):
        self.borrowList = []

    def searchBook(self, book, lib):
        for item in lib:
            if book == item:
                print("Item found")
                return True
        return False
    def borrowBook(self, book, lib):
        if self.searchBook(book, lib):
            print("Book borrowed")
            self.borrowList.append(book)
    def returnBook(self, book):
        self.borrowList.remove(book)
        print("Book returned")

class Librarian(libEditCatalog, libSearch, libBorrow, libReport):
    def __init__(self):
        self.borrowList = []

    def addBook(self, book, lib):
        lib.append(book)
        print("Book added to catalog")
    def removeBook(self, book, lib):
        lib.remove(book)
        print("Book removed from catalog")

    def searchBook(self, book, lib):
        for item in lib:
            if book == item:
                print("Item found")
                return True
        print("Item not found")
        return False
    def borrowBook(self, book, lib):
        if self.searchBook(book, lib):
            print("Book borrowed")
            self.borrowList.append(book)
    def returnBook(self, book):
        self.borrowList.remove(book)
        print("Book returned")
    def generateReport(self):
        print("Report generate")

def demo():
    lib = ['book1', 'book2', 'book3']
    guest = Guest()
    user1 = User()
    admin1 = Librarian()

    guest.searchBook('book1', lib)
    user1.searchBook('book1', lib)
    admin1.searchBook('book1', lib)

    print('\n')

    #guest.borrowBook('book1', lib) <--- throws error
    user1.borrowBook('book1', lib)
    user1.returnBook('book1')
    admin1.borrowBook('book1', lib)
    admin1.returnBook('book1')

    print('\n')

    admin1.addBook('book4', lib)
    admin1.removeBook('book4', lib)
    
    print('\n')

    admin1.generateReport()

if __name__ == "__main__":
    demo()