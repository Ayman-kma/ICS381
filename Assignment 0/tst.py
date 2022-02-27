from turtle import bk
import class_practice

bk = class_practice.Bookstore({}, {}, {})
bk.addBook("asdf", 10, 50)
bk.addBook("asdf", 1000, 50)
bk.addBook("asdff", 10, 50)
bk.addBook("asdffff", 10, 50)
print(bk.getQuantity("asdf"))
bk.addQuantity("asdf", 69)
print(bk.getQuantity("asdf"))
