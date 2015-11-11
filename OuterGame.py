from InnerGame import InnerGame
from Board import Board
from GameChecker import GameChecker
import os
from collections import OrderedDict
import colorama
from colorama import Fore, Back, Style
from random import randint


colorama.init()

game1 = InnerGame(55)
game2 = InnerGame(56)
game3 = InnerGame(57)
game4 = InnerGame(52)
game5 = InnerGame(53)
game6 = InnerGame(54)
game7 = InnerGame(49)
game8 = InnerGame(50)
game9 = InnerGame(51)

gamesRemaining = [49, 50, 51, 52, 53, 54, 55, 56, 57]

selectGame = {55: game1, 56: game2, 57: game3,
	          52: game4, 53: game5, 54: game6,
		      49: game7, 50: game8, 51: game9}

gameBoards = [{55: game1.board, 56: game2.board, 57: game3.board},
             {52: game4.board, 53: game5.board, 54: game6.board},
             {49: game7.board, 50: game8.board, 51: game9.board}]           

gameBoards[0] = OrderedDict(sorted(gameBoards[0].items()))

completeGames = []
playerOne = 'X'
playerTwo = 'O'
onesGo = True
gameOn = True
# start in center square
currentBoard = 53
playerWins = {'X': [], 'O': []}

checkGame = lambda player, playerWins: GameChecker.checkGame(player, playerWins)
clear = lambda: os.system('cls')
clear()
printBoard = lambda playerWins: Board.printBoard(gameBoards, currentBoard, playerWins)
printBoard(playerWins)


# GAME LOOP
while gameOn:
	player = playerOne if onesGo else playerTwo
	colour = Fore.WHITE + Back.RED if player is 'X' else Fore.WHITE + Back.GREEN
	print('\n\n\n'+ colour + player + "'s" + Back.RESET + Fore.RESET + ' go!')
	
	game = selectGame[currentBoard]
	gameNumber = game.gameNumber

	if game.makeChoice(player):		
		onesGo = not onesGo
		clear()		

		if game.checkGame():
			# add to finished games
			completeGames.append(gameNumber)
			playerWins[player].append(gameNumber)
			gamesRemaining.remove(gameNumber)
			# check if main game is won
			if checkGame(player, playerWins):
				clear()
				currentBoard = 0
				printBoard(playerWins)
				print('\n\n'+ player +' is the winner!')
				break

		# select correct board
		# if choice is in complete games stay in current game
		if game.choice in completeGames:
			# if current board is complete, pick random remaining board
			if currentBoard in completeGames:
				# random 
				# NEEDS TO BE random thats not the current unless its only one left
				# while else? with tempBoard = current board
				currentBoard = gamesRemaining[randint(0, len(gamesRemaining) - 1)]
				# OR players choice, but takes up go, chooses next players location
		else:
			# else move to choice square
			currentBoard = game.choice

		printBoard(playerWins)