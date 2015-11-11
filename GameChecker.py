

"""
GameChecker
-----------
The GameChecker class checks if the outer game has been
won, this determines the winner of the whole game 

"""


class GameChecker:

	# checkGame takes in the player, and a list of the players
	# wins, the players wins are basically the Dec value of
	# the key used to select the particular square on the grid
	def checkGame(player, playerWins):
		# extract players wins from list
		wins = playerWins[player]

		# horizontal check
		# check to see if a whole horizontal row is in
		# the platers wins, do for each row, if there is
		# then return true to signify a win
		if 55 in wins and 56 in wins and 57 in wins:
			return True
		elif 52 in wins and 53 in wins and 54 in wins:
			return True
		elif 49 in wins and 50 in wins and 51 in wins:
			return True
		# vertical check
		# same idea as above only for vertical columns
		elif 55 in wins and 52 in wins and 49 in wins:
			return True
		elif 56 in wins and 53 in wins and 50 in wins:
			return True
		elif 57 in wins and 54 in wins and 51 in wins:
			return True
		# diagonal check
		# same idea as above only for the diagonal rows
		elif 55 in wins and 53 in wins and 51 in wins:
			return True
		elif 49 in wins and 53 in wins and 57 in wins:
			return True
		# if no win is found, return false to signify no wins
		else:
			return False		
		