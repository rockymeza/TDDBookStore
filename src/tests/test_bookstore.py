import unittest
from bookStore import BookStore

class Test(unittest.TestCase):
    
    def test_buy_one_book_in_each_five_kinds(self):        
        book_store = BookStore()
        cost = book_store.buy([1,1,1,1,1])
        self.assertEqual(30, cost, 'cost should be 30 against ' + str(cost))
        
    def test_buy_one_book_in_one_kind(self):        
        book_store = BookStore()
        cost = book_store.buy([1,0,0,0,0])
        self.assertEqual(8, cost, 'cost should be 8 against ' + str(cost))
        
    def test_buy_one_book_in_each_two_kinds(self):        
        book_store = BookStore()
        cost = book_store.buy([1,1,0,0,0])
        self.assertEqual(15.2, cost, 'cost should be 15.2 against ' + str(cost))
        
    def test_buy_one_book_in_each_three_kinds(self):
        book_store = BookStore()
        cost = book_store.buy([1,1,1,0,0])
        self.assertEqual(21.6, cost, 'cost should be 21.6 against ' + str(cost))
        
    def test_buy_one_book_in_each_four_kinds(self):
        book_store = BookStore()
        cost = book_store.buy([1,1,1,1,0])
        self.assertEqual(25.6, cost, 'cost should be 25.6 against ' + str(cost))
        
    def test_buy_nothing(self):
        book_store = BookStore()
        cost = book_store.buy([0,0,0,0,0])
        self.assertEqual(0, cost, 'cost should be 0 against ' + str(cost))
        
    def test_buy_two_books_in_one_kind(self):
        book_store = BookStore()
        cost = book_store.buy([2,0,0,0,0])
        self.assertEqual(16, cost, 'cost should be 16 against ' + str(cost))
    
    def test_buy_as_22211(self):
        book_store = BookStore()
        cost = book_store.buy([2,2,2,1,1])
        self.assertEqual(51.6, cost, 'cost should be 51.6 against ' + str(cost))