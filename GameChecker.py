

class GameChecker:

	def checkGame(player, playerWins):
		# check if main game is won
		wins = playerWins[player]
		# HORIZONTAL
		if 55 in wins and 56 in wins and 57 in wins:
			return True
		elif 52 in wins and 53 in wins and 54 in wins:
			return True
		elif 49 in wins and 50 in wins and 51 in wins:
			return True
		# VERTICAL
		elif 55 in wins and 52 in wins and 49 in wins:
			return True
		elif 56 in wins and 53 in wins and 50 in wins:
			return True
		elif 57 in wins and 54 in wins and 51 in wins:
			return True
		# DIAGONAL
		elif 55 in wins and 53 in wins and 51 in wins:
			return True
		elif 49 in wins and 53 in wins and 57 in wins:
			return True
		else:
			return False		
		