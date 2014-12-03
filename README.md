TDDBookStore
============
Description:

To try and encourage more sales of the 5 different Harry
Potter books they sell, a bookshop has decided to offer
discounts of multiple-book purchases.

One copy of any of the five books costs 8 EUR.

If, however, you buy two different books, you get a 5%
discount on those two books.

If you buy 3 different books, you get a 10% discount.

If you buy 4 different books, you get a 20% discount.

If you go the whole hog, and buy all 5, you get a huge 25%
discount.

Note that if you buy, say, four books, of which 3 are
different titles, you get a 10% discount on the 3 that
form part of a set, but the fourth book still costs 8 EUR.

Your mission is to write a piece of code to calculate the
price of any conceivable shopping basket (containing only
Harry Potter books), giving as big a discount as possible.

For example, how much does this basket of books cost?

2 copies of the first book
2 copies of the second book
2 copies of the third book
1 copy of the fourth book
1 copy of the fifth book

Answer: 51.60 EUR

第一问 / Question 1
-------------------

仅支持每种书要么买一本，要么一本都不买，求总价。

样例输入： ``[1, 0, 0, 0, 0]``

样例输出： ``8``

The system only needs to support selling each book once. You can either sell it
or not sell it. Please return the total price.

Sample input: ``[1, 0, 0, 0, 0]``

Sample output: ``8``

第二问 / Question 2
-------------------

支持每种书买任意本，求总价。

样例输入： ``[2, 2, 2, 1, 1]``

样例输出： ``51.60``

The system supports selling any number of each book. Please return the total
price.

Sample input: ``[2, 2, 2, 1, 1]``

Sample output: ``51.60``
