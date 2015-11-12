from InnerGame import InnerGame
from Board import Board
from GameChecker import GameChecker
import os
from collections import OrderedDict
import colorama
from colorama import Fore, Back, Style
from random import randint


"""
OuterGame
---------
The OuterGame is where the game is controlled from, it
contains the logical flow of the program. This is the file
that is ran to play the game.

"""


colorama.init()

# creating the 9 inner game objects
# the number passed to the constructor
# is an identification number and also
# the Dec value of the boads grid postion
# related to the number pad
game1 = InnerGame(55)
game2 = InnerGame(56)
game3 = InnerGame(57)
game4 = InnerGame(52)
game5 = InnerGame(53)
game6 = InnerGame(54)
game7 = InnerGame(49)
game8 = InnerGame(50)
game9 = InnerGame(51)

# contains the remaining unfinished games
# starts with all games remaining
gamesRemaining = [49, 50, 51, 52, 53, 54, 55, 56, 57]

# used to select the current game to operate on
# the currentBoard variable will contain the number
# of the current board, this selects the game from
# the selectGame dictionary
selectGame = {55: game1, 56: game2, 57: game3,
	          52: game4, 53: game5, 54: game6,
		      49: game7, 50: game8, 51: game9}

# contains the board states of all the inner game boards
# this is used to print the game board
gameBoards = [{55: game1.board, 56: game2.board, 57: game3.board},
             {52: game4.board, 53: game5.board, 54: game6.board},
             {49: game7.board, 50: game8.board, 51: game9.board}]           

# the first element of the gameBoards was unordered because
# Python dictionaries are unordered. I had to manually order
# the first element, coincedentally, the other elements were
# in order
gameBoards[0] = OrderedDict(sorted(gameBoards[0].items()))

# store the complete games (finished or won games)
completeGames = []
# player symbols, this is what is printed
# inside taken inner game squares
playerOne = 'X'
playerTwo = 'O'
# true if it is player ones go
onesGo = True
# true while the game has not been won yet
gameOn = True
# stores the currently active board number 
# start in the center square
currentBoard = 53
# store the numbers of won boards for each player
playerWins = {'X': [], 'O': []}

# creating an easier to write function for game checking
# takes the player and playerWins dictionary as arguments
checkGame = lambda player, playerWins: GameChecker.checkGame(player, playerWins)
# creating an easier to write function for clearing the console screen
clear = lambda: os.system('cls')
# clear it before starting the game
clear()
# creating an easier to write function for printing the game board
# the lambda function takes in playerWins only, but the full function takes
# in gameBoards, currentBoard and playerWins
printBoard = lambda playerWins: Board.printBoard(gameBoards, currentBoard, playerWins)
# print the board for start of game
printBoard(playerWins)


# GAME LOOP
# this loop keeps running until the game is won or quit
while gameOn:
	# choose the player
	# if onesGo is true, select playerOne
	# if onesGo is false, select playerTwo
	player = playerOne if onesGo else playerTwo
	# set players colour
	colour = Fore.WHITE + Back.RED if player is 'X' else Fore.WHITE + Back.GREEN
	# tell the user whos go it is
	print('\n\n\n'+ colour + player + "'s" + Back.RESET + Fore.RESET + ' go!')
	
	# use the currentBoard number to select 
	# the corresponding game object
	game = selectGame[currentBoard]
	# set the game number, easier to write
	gameNumber = game.gameNumber

	# allow the player to make a choice, pass the player symbol
	# to the makeChoice function, if a valid choice is made the
	# player symbol will be place in the chosen inner game square
	# and the function will return true. The user will be prompted
	# of errors and will have to make a valid choice in order for
	# the game to continue
	if game.makeChoice(player):		
		# make onesGo false so playerTwo will
		# be selected next time around
		# (not True == False)
		# (not False == True)
		onesGo = not onesGo
		# clear the console screen
		clear()		

		# check if the current inner game has been won
		# returns True if the inner game has been won
		# False if not
		if game.checkGame():
			# if inner game has been won add
			# game number to finished games
			completeGames.append(gameNumber)
			# add game number to individual player wins
			playerWins[player].append(gameNumber)
			# remove game number from remaining games
			gamesRemaining.remove(gameNumber)
			# check if the outer game has been won
			# returns True if outer game has been won
			# False if not			
			if checkGame(player, playerWins):
				# clear screen
				clear()
				# reset current board to 0
				currentBoard = 0
				# print out the board
				printBoard(playerWins)
				# print winning message
				print('\n\n'+ player +' is the winner!')
				# break out of the game loop, ending the game
				break

		# select next playable board
		# if current inner game choice is in complete  
		# games then stay in current game
		if game.choice in completeGames:
			# if current board is complete, pick random remaining board
			if currentBoard in completeGames:
				# random current board, this will be 
				# the active board on the next turn
				currentBoard = gamesRemaining[randint(0, len(gamesRemaining) - 1)]
		else:
			# else move to choice square
			# next active inner game will correspond
			# to the players choice position
			currentBoard = game.choice

		# print the board
		printBoard(playerWins)