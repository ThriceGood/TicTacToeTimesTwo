import colorama
from colorama import Fore, Back, Style


"""
Board
-----
The Board class prints out the game boards to the console,
it is updated and reprinted after each turn

"""


class Board:

	# prints out the game boards, takes in the allBoards list
	# which contains the seperate InnerGame object board values,
	# the currentBoard, used to highlight the board currently in
	# play, and the wins list, containing the positions that the
	# players have won
	def printBoard(allBoards, currentBoard, wins):	

		rowString = ''
		rowStrings = []
		print('\n')

		# the idea here is to iterate through the allBoards list, then iterate through a
		# range of 1 - 3, then iterate through the boards at the current allBoards element
		# then decide what string to concatenate to the row string.
		# the allBoards list contains three elements, each of which representing the three
		# horizontal board groups, or three lists of three board values, the values being
		# either ' ', 'X' or 'O'
		# the first loop iterates through these horizontal rows (three times)
		# the next loop iterates through a range of 1 - 3, this is needed to use the 'i' value
		# the next loop iterates through the trio of boards at the current allBoards element
		# these boards represent the first horizontal row of the outer board
		# using the 'i' value from the middle loop, the rows of the inner boards are selected
		# and concatenated to the row string
		# the combination of loops works its way through all the inner boards and prints out
		# each row and value contained in each square
		# if the board is the current board, the board is highlighted white to indicate the active board
		# if player X has won that particular board, it is highlighted red
		# if player Y has won that particular board, it is highlighted green
		# else the board is not highlighted

		for boards in allBoards:
			for i in range(1, 4):
				for number, board in boards.items():								
					if number == currentBoard:	
						rowString += Back.WHITE + Fore.BLACK + board[i][1] +'|'+ board[i][2] +'|'+ board[i][3] + Back.RESET + Fore.RESET + ' | '		
					elif number in wins['X']:
						rowString += Back.RED + Fore.WHITE + board[i][1] +'|'+ board[i][2] +'|'+ board[i][3] + Back.RESET + Fore.RESET + ' | '
					elif number in wins['O']:
						rowString += Back.GREEN + Fore.WHITE + board[i][1] +'|'+ board[i][2] +'|'+ board[i][3] + Back.RESET + Fore.RESET + ' | '
					else:
						rowString += board[i][1] +'|'+ board[i][2] +'|'+ board[i][3] + ' | '
				# append the rowString to the list of rowStrings
				# to be used to print the board
				rowStrings.append(rowString[:-3])
				# reset the string
				rowString = ''

		i = 1
		# iterate through the list of rowStrings
		for string in rowStrings:
			# print the row string
			print(string)
			# every three rows print the horizontal
			# line of the outer board, except after
			# the final three rows
			if i % 3 == 0 and i != 9:
				print('---------------------')
			i += 1




