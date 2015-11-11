import colorama
from colorama import Fore, Back, Style


class Board:

	def printBoard(allBoards, currentBoard, wins):	

		rowString = ''
		rowStrings = []
		print('\n')

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
				rowStrings.append(rowString[:-3])
				rowString = ''

		i = 1
		for string in rowStrings:
			print(string)
			if i % 3 == 0 and i != 9:
				print('---------------------')
			i += 1




