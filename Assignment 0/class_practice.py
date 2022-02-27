class Bookstore:
    def __init__(self, book_list, quantity_list, price_list):
        self.book_list = book_list
        self.quantity_list = quantity_list
        self.price_list = price_list
        self.book_dict = dict()
        for i in range(len(book_list)):
            self.addBook(book_list[i], quantity_list[i], price_list[i])

    def addBook(self, book_name, quantity, price):
        if book_name not in self.book_dict:
            self.book_dict[book_name] = [quantity, price]

    def addQuantity(self, book_name, quantity):
        if book_name in self.book_dict:
            self.book_dict[book_name][0] += quantity

    def adjustPrice(self, book_name, price):
        if book_name in self.book_dict:
            self.book_dict[book_name][1] = price

    def getQuantity(self, book_name):
        if book_name in self.book_dict:
            return self.book_dict[book_name][0]
        else:
            return None

    def getPrice(self, book_name):
        if book_name in self.book_dict:
            return self.book_dict[book_name][1]
        else:
            return None
