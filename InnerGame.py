from collections import OrderedDict
from msvcrt import getch


"""
InnerGame
---------
The InnerGame object is a TicTacToe game object that
encapsulates the data and functions of a single TicTacToe
game. In the 'OuterGame', nine of these objects are created,
one for each square of the main TicTacToe game.

"""


class InnerGame:

	# object constructor takes in gameNumber for identification
	def __init__(self, gameNumber):		
		self.gameNumber = gameNumber

		# game board, stores the player symbols in 
		# taken squares used for printing the board
		self.board = {1: {1: ' ', 2: ' ', 3: ' '}, 
					  2: {1: ' ', 2: ' ', 3: ' '}, 
					  3: {1: ' ', 2: ' ', 3: ' '}}
		
		# possible choices and board locations
		# each number is the Dec value of the keys '1' to '7', a player uses these
		# keys to select the square they wish to take, the x and y values are the
		# choices square location on the grid
		self.choices = {55: {'x': 1, 'y': 1}, 56: {'x': 1, 'y': 2}, 57: {'x': 1, 'y': 3},
			            52: {'x': 2, 'y': 1}, 53: {'x': 2, 'y': 2}, 54: {'x': 2, 'y': 3},
	 			        49: {'x': 3, 'y': 1}, 50: {'x': 3, 'y': 2}, 51: {'x': 3, 'y': 3}}					 

	 	# standard Python dictionaries are not ordered, so i must create
	 	# an OrderedDict in order to have order!
		self.board = OrderedDict(sorted(self.board.items()))
		# append taken squares to this list, for use in deciding which
		# squares a player can not take (already taken)
		self.taken = []
		# the platers choice
		self.choice = 0
		# gameFull is set to true when all squares are taken
		self.gameFull = False



	# prompts the user to make a choice, pick a square to take
	# takes in the player symbol (X, O)
	def makeChoice(self, player):
		print('\n')

		# keep asking a user to make a choice until a valid
		# choice is made
		while True:
			# prompt
			print('Use the number pad to select square:')
			# use getch() to get the char of a pressed key,
			# use ord() to convert it to its Dec value
			choice = ord(getch())

			# pass the choice to checkChoice() to 
			# validate the choice, if it returns true
			# then a valid choice was made
			if self.checkChoice(choice):
				# store the choice as a property				
				self.choice = choice
				# extract the x and y grid values
				# from the choices dictionary				
				x = self.choices[choice]['x']
				y = self.choices[choice]['y']
				# set the player symbol to the square 
				self.board[x][y] = player
				# break the loop to end the makeChoice procedure
				break
			else:
				# if choice does not validate, try again
				pass

		# return true to signify choice was made
		return True



	# validates a players choice, takes in the choice value
	def checkChoice(self, choice):
		# error string
		errors = ''

		# 113 = 'q', quits game
		if choice == 113:
			quit()

		# choices outside of the specified values do not count
		if choice < 49 or choice > 57:
			errors += 'not a choice'

		# if choice is in list of take squares 
		# then not a valid choice
		if choice in self.taken:
			errors += 'sqaure is taken'

		# if length of error string is > 0
		# then there has been an error,
		# print error message and return false (invalid)
		if len(errors) > 0:
			print('\n'+errors+', try again'+'\n')
			return False
		else:
			# if no errors, add current choice to list
			# of taken squares and return true (valid)
			self.taken.append(choice)
			return True



	# checks if this particular game has been won or filled (draw)
	def checkGame(self):
		board = self.board		
		empty = 0

		# find out if board is full
		# iterate board rows
		for row, squares in board.items():
			# iterate board columns
			for col, square in squares.items():
				# if square is empty then increment 
				# square empty counter
				if square is ' ':
					empty += 1

		# if there is no empty squares then
		# the game is full and cant be selected
		# as a choice in the outer game
		if empty is 0:
			self.gameFull = True


		# run the game check for each player
		for player in ['X', 'O']:

			# horizontal check
			# iterate the rows of the board
			for row, squares in board.items():
				# if a full row is taken by a player
				# then return true to signify that
				# the game has been won
				if  squares[1] == player \
				and squares[2] == player \
				and squares[3] == player:
					return True

			# vertical check
			# to check if a full vertical column is taken
			# by a player, iterate through a range of 1-3
			# i will be 1 on the first iteration, then 
			# iterate through the rows of the board using
			# i to check the value of the square, when i
			# is 1, the first square of each row will be
			# checked, when i is 2, the second sqaure will
			# be checked and so on. If the players symbol
			# is found in the square then increment the counter,
			# if the counter is equal to 3 then a full vertical
			# row was taken by the player and that player wins!	
			for i in range(1, 4):
				count = 0
				for row, squares in board.items():
					if squares[i] is player:
						count += 1
					if count == 3:
						return True

			# check the two possible diagnals

			# diagonal 1, top left to bottom right
			count = 0
			tics = 0
			# iterate board rows, and use the counter to
			# check the square, increment tics if player
			# symbol is found in square, as counter increases
			# next square is selected
			for row, squares in board.items():
				count += 1
				if squares[count] == player:
					tics += 1

			# player wins if tics equal 3
			if tics == 3:
				return True		

			# diagonal 2, top right to bottom left
			# same as above only in reverse direction
			count = 4
			tics = 0
			for row, squares in board.items():
				count -= 1
				if squares[count] == player:
					tics += 1

			if tics == 3:
				return True			


