#!/usr/bin/python

import argparse


def find_max_profit(prices):
    current_min_price = prices[0]
    print(current_min_price)
    max_profit = prices[1] - current_min_price
    print(max_profit)
    n = len(prices)

    for i in range(n):
        for j in range(i + 1, n):
            print(prices[j], prices[i], max_profit)
            if max_profit < prices[j] - prices[i]:
                max_profit = prices[j] - prices[i]
    return max_profit


#     max_profit = float('-inf')
#     n = len(prices)
#     for i in prices:
#         for j in range(i + 1, n):
#             if i < prices[j]:
#                 temp_profit = prices[j] - i
#                 if temp_profit > max_profit:
#                     max_profit = temp_profit
#             else:
#                 temp_profit = prices[j] - i
#                 if temp_profit > max_profit:
#                     max_profit = temp_profit
#     return max_profit


'''
10 20
Instantiate max-profit variable = -infinity
Iterate through all the values in our input, i
Iterate through all subsequent values, not including the first / current value in list, j
If difference between j and i is greater than current max profit, then
Set max_profit equal to what we find from this difference between j and i
Return max-profit value
'''

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
