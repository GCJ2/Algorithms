import unittest
from stock_prices import find_max_profit


class Test(unittest.TestCase):

    def test_find_max_profit(self):
        self.assertEqual(find_max_profit([10, 7, 5, 8, 11, 9]), 6)
        self.assertEqual(find_max_profit([100, 90, 80, 50, 20, 10]), -10)
        self.assertEqual(find_max_profit([1050, 270, 1540, 3800, 2]), 3530)
        self.assertEqual(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]), 94)


if __name__ == '__main__':
    unittest.main()

'''
Loop through list and find highest number if index is not [-1]
Loop through list before highest number to find lowest number
If highest number index == [1], check next element
For i in range of list: if i > i+1 and index(i+1) == -1:
Buy price == i[-2] sell price == i[-1]
'''

'''
profit = 0
for i in list:
profit = 
'''

'''
All of the above is terrible
profit = 0
min_price = list[0]
Start an list[0]
For price in prices
set min_price to whatever is smaller, price, or current index
subtract min_price from price for profit_comparison
A[0] = 5; A[1] = 10; A[2] = 20
min_price = 5; price = 10; profit_comparison = 5
set profit to whatever is higher between current profit and profit_comparison 
'''