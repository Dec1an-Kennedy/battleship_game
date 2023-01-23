from random import randint

#Board for ship locations
hidden_board = [[" "] * 8 for x in range(8)]
#Board for displaying hits and misses
guess_board = [[" "] * 8 for i in range(8)]