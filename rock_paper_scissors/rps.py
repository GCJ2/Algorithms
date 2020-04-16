#!/usr/bin/python

import sys


def rock_paper_scissors(n):
	rps = ['rock', 'paper', 'scissors']
	plays = []

	def game(n, play=[]):
		print(f'plays 11: {play}')
		if n == 0:
			plays.append(play)
			# This will append an empty lit
			return
		for moves in rps:
			# for every item in rock paper scissors
			game(n - 1, play + [moves])
			# run game() again but add move to the play list
			# this will loop through the rps list again
			# and add each value
			pm = play + [moves]
			print(f'play: {play} moves: {[moves]}')

	game(n, [])
	print(plays)
	return plays


rock_paper_scissors(2)


if __name__ == "__main__":
	if len(sys.argv) > 1:
		num_plays = int(sys.argv[1])
		print(rock_paper_scissors(num_plays))
	else:
		print('Usage: rps.py [num_plays]')
