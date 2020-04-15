#!/usr/bin/python

import argparse


def find_max_profit(prices):
    profit = 0
    sell_price = prices[0]

    for price in prices:
        sell_price = min(sell_price, price)
        profit_comparison = price - sell_price
        profit = max(profit_comparison, profit)

    # gunna try to brute force it
    # I'm sorry Big O
    # I have failed you

    # for i in range(prices):

    return profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
