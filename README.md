# CS161FinalProject
Final project for CS161 class at OSU in the Fall of 2019
# project-10

Write a class named FBoard for playing a game, where player x is trying to get her piece to row 7 and player o is trying to make it so player x doesn't have any legal moves.  It should have the following private data members:

* An 8x8 list of lists for tracking what's on each square of the board.
* A data member for tracking the game state, that holds one of the following string values: "X_WON", "O_WON", or "UNFINISHED".
* Data members to keep track of where the x piece is.

**The data members should all be private.**
* An init method (constructor) that initializes the list of lists to represent an empty 8x8 board (you can use whatever character you want to represent empty).  It should then put four o pieces on row 7, in columns 0, 2, 4, and 6.  It should put an x piece on row 0, column 3.  It should also initialize the other data members.
* A method called get_game_state, that returns the current value of game_state.
* A method called move_x that takes as parameters the row and column of the square to move to.  If the desired move is not allowed, or if the game has already been won, it should just return false.  Otherwise it should make the move and return true.  A piece belonging to x can move 1 square diagonally in any direction.  A piece is not allowed to move off the board or to an occupied square.  If x's move gets her piece to row 7, game_state should be set to "X_WON".
* A method called move_o that takes as parameters the row and column to move from, and the row and column to move to.  If the first pair of coordinates doesn't hold o's piece, or if the desired move is not allowed, or if the game has already been won, it should just return false.  Othewise it should make the move and return true.  A piece belonging to o can move 1 square diagonally, **but the row cannot increase**, so any o piece has at most two available moves.  For example, if player o has a piece at (5, 2), it could move to (4, 1) or (4, 3), but not (6, 1) or (6, 3).  It is not allowed to move off the board or to an occupied square.  If o's move leaves no legal move for x, game_state should be set to "O_WON".

You do not need to track whose turn it is.  Either move method can be called multiple times in a row.

It doesn't matter which index of the list of lists you consider the row and which you consider the column as long as you're consistent.

Feel free to add helper functions if you want.  You may also find it useful to add a print function to help with debugging.

Here's a very simple example of how the class could be used:
```
   fb = FBoard();
   fb.move_x(1,4);
   fb.move_x(2,5);
   fb.move_o(7,0,6,1);
   print(fb.get_game_state());
```
The file must be named: **FBoard.py**
