# TicTacToeTimesTwo
Its TicTacToe only Twice as crazy!!!


To play, run OuterGame.py


How to play
-----------

The first player to go is always X. You must use the number pad to select the
location inside the inner highlited grid, this is called the 'inner game', the 
larger outer grid is called the 'outer game'. The number pad positions exaclty
correspont to the grid locations, so the number 7 is the top left grid position,
the number 5 is the center position, the number 3 is the bottom right position
and so on. 

![alt tag](https://raw.githubusercontent.com/ThriceGood/TicTacToeTimeTwo/master/images/1.png)


The position chosen by X in the inner game determines where the next active inner
game will be on the outer game grid. O's turn will be in that inner game. If X 
decides to take the 6 position (middle right), then the next inner game will be
in the 6 position of the outer game. This is where O must take its turn.

![alt tag](https://raw.githubusercontent.com/username/projectname/master/images/2.png)


The same rule applies to the next player. The choice they make determines the next
players position in the outer game. Below, O choice the 8 position on the inner game
so the X's next go is in the 8 position on the outer game.

![alt tag](https://raw.githubusercontent.com/username/projectname/master/images/3.png)


The obejct of regular 'TicTacToe' is for a player to take three squares in a row
to win the game. Each inner game follows these regular Tic Tac Toe rules.
The object of 'TicTacToeTimesTwo' is similar, only to win the game a player must
take three of the 'outer game' squares in a row, to take on outer game square a 
player must win the inner game at that position on the outer game.

![alt tag](https://raw.githubusercontent.com/username/projectname/master/images/4.png)


The best strategy is one that manoeuvres your self and your opponent around the outer
board in a way that enables you to take three inner games in a row. These leads to 
very interesting and strategic game play. When the board starts to fill up with taken
squares, your moves need to be taken with care not to place your opponent into an inner
game that they could win with one move. The more the board fills, the harder this gets.
An interesting and fun result is that you could place your opponent into an inner game
that they could win with one move, but they choose to take a square that doesnt win the
game because picking the inner game winning square may place you into a position to win 
the outer game, thus winning the whole game. Choosing to win an inner game may set off
an explosive chain reaction of game wins from both players! So you must look ahead an
consider you and your opponents options. It looks like O may win this one!

![alt tag](https://raw.githubusercontent.com/username/projectname/master/images/5.png)


nope, X takes it in the end!

![alt tag](https://raw.githubusercontent.com/username/projectname/master/images/6.png)




Other Rules
-----------

If a players choice places the next game into an already won game, then the next move
will be played inside of the current game. If the current game is also taken then a 
random game will be chosen from the list of unfinished games. This can sometimes lead
to deadlocks, draws, no winners, sad faces and waste of time! 
