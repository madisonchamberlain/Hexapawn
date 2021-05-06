# Hexapawn

## What the code does:
This code uses artificial intelligence to find the next best move for a player to make in a game called hexapawn (rules below). The solution is found using minimax propogation where negative points are generated for an opponents move and positive moves are generated for the players move.  On the players turn, the most positive score is propogated up and on the opponents turn, the most negative score is propogated up.  

## Rules of the game:
Hexapawn is played on an n x n chessboard.  The two players face each other across the board. N white players start at the top row of the board, and n black players start at the bottom row.  The white player always moves first.  Pawns can either be moved one square straight towards the opponents side, or one diagonal if the opponent has a piece placed there.  Moving ontop of an opponent removes their pawn from the board. The game contunues until someone wins.  A win takes place when one of the following happens: A player reaches the opponents side of the board, a player has prevented the opponent from being able to move, and a player has taken the last pawn of the opponent.

## How the function works:
The hexapawn function takes in a current board, the dimension of the board, the number of moves to look foward, and whose turn it is.  It returns the best move for the player whose turn it is to make a move.  

## Static board evaluation function:
The "goodness" of a move is evaluated as follows. If the player whose turn it is to move wins, a board gets +10 points. If the opponent wins, the board recieves -10 points.  If nobody wins the score is calculated as follows: number of player pawns with a clear path - number of opponent pawns with a clear path + number of player pawns - number of opponent pawns.  A clear path is when a player has nothing in between it and the opponents side.  This does not take into account anything diagonal of the player; only things directly ahead of the player.  
