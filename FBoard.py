# Project 10
# Author: Christopher Eckerson
# Date: 12/5/2019
# Description: Creates a class called "FBoard" which initializes the 8x8 board
#   with starting positions for the "x" and "o player, the game state to UNFINISHED,
#   and records the current position and possible moves of the "x" player.
#
#   Contains a method (move_x) to allow "x" player to move their piece,
#   a method (move_o) to allow "o" player to move one of their pieces,
#   a method to get the current game state,
#   an optional method that prints the rules of the game,
#   and an optional method to display the Fboard game in the console.
#
#   The move_x and move_o methods will check if the move is allowed,
#   remove the previous location from the board of that player's piece,
#   and update the board with the new position.
#   Additionally, each method checks if that player has won the game.


class FBoard:
    """Represents a game of FBoard"""

    def __init__(self):
        """
        Initializes a game of Fboard with a board,
        with starting positions of "x" piece and "o" pieces
        Initializes the current state, "x" position & directions of motions,
        and two variables for checking if "o" player won
        """
        # Create board, represented by a list of 8 lists of length 8 with starting positions of "x" and "o"
        self._board = [[" ", " ", " ", "x", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "],
                       ["o", " ", "o", " ", "o", " ", "o", " "]]
        # Start game state as unfinished
        self._game_state = "UNFINISHED"
        # Record position of "x" piece on board
        self._x_position = (0, 3)
        # Record the "x" piece possible directions of motion (before checking if allow)
        self._x_directions = [(-1, 2), (-1, 4), (1, 4), (1, 2)]
        # Unless function move_o uses function move_x to check if x has allowed moves, set to FALSE
        self._O_WON_check = False
        # Function move_o checks if "x" has allowed moves, iterating if "x" does
        self._allowed_moves = 0

    def get_game_state(self):
        """Allows user to return value of game state"""
        return self._game_state

    def move_x(self, row, column):
        """
        Takes in the row and column the "x" player would like to move to.
        Checks if allowed (returns False if not), then updates board
        and x position & directions of possible moves.
        Finally, checks if "x" player has reached the 7th row (winning the game),
        then returns True.
        :param row:
        :param column:
        :return False or True:
        """
        # Checks if move is within the boundaries of the board
        if row < 0 or row > 7:
            return False
        if column < 0 or column > 7:
            return False
        # Checks if position is already occupied
        if self._board[row][column] == "o":
            return False
        # Checks if game is already won
        if self._game_state != "UNFINISHED":
            return False
        # Checks if moves is one of the possible "x" movements
        if (row, column) in self._x_directions:
            # Checks that the move_o function didn't call the move_x function
            if not self._O_WON_check:
                # For the allowed move played by the "x" player
                # Removes "x" from the previous location on the board
                self._board[self._x_position[0]][self._x_position[1]] = " "
                # Updates board with new location of "x"
                self._board[row][column] = "x"
                # Updates position of "x"
                self._x_position = (row, column)
                # Updates possible "x" movements at the new location
                self._x_directions = [(row - 1, column - 1), (row - 1, column + 1), (row + 1, column + 1),
                                      (row + 1, column - 1)]
                # If "x" player reaches the 7th row, change game state
                if row == 7:
                    # "x" player won, update game state
                    self._game_state = "X_WON"
                # "x" player move was allowed returns True
                return True
            # If move_o function called move_x function, and "x" has still has allowed moves
            else:
                # Iterates allowed moves for the number of allowed moves "x" still has
                self._allowed_moves += 1
        # Position picked does not match allowed possible "x" moves
        else:
            return False

    def move_o(self, from_row, from_column, to_row, to_column):
        """
        Takes in the current position (from_row and from_column) of a "o" player location
        and also the position (to_row and to_column) where that "o" player will be moved to.
        Checks if current position contains an "o" player and if the position moved to
        is allowed (returns False if not), then updates board with "o" new position
        Finally, checks if "x" player has any allowed moves after "o" player moves (winning the game),
        then returns True.
        :param from_row:
        :param from_column:
        :param to_row:
        :param to_column:
        :return False or True:
        """
        # Checks if move is within the boundaries of the board
        if to_row < 0:
            return False
        if to_column < 0 or to_column > 7:
            return False
        # Checks if current position contains an "o" player
        if self._board[from_row][from_column] != "o":
            return False
        # Checks if new position is already occupied
        if self._board[to_row][to_row] != " ":
            return False
        # Checks if game is already won
        if self._game_state != "UNFINISHED":
            return False
        # Checks if "o" row value is not increasing
        if from_row == to_row + 1:
            # Checks if "o" column is a diagonal move
            if from_column == to_column + 1 or from_column == to_column - 1:
                # Removes "o" from the previous position on the board
                self._board[from_row][from_column] = " "
                # Updates board with current position of "o" player
                self._board[to_row][to_column] = "o"
            # If not a diagonal move
            else:
                return False
        # If row value is increasing
        else:
            return False
        # Check if "o" won the game, set "o" win check variable to true, used when calling move_x function
        self._O_WON_check = True
        # Checks all four possible moves of the "x" player
        for allowed_moves in self._x_directions:
            # Calls move_x function, input possible move of "x" to see if move is allowed
            self.move_x(allowed_moves[0], allowed_moves[1])
        # If "x" player doesn't have any allowed moves available
        if not self._allowed_moves > 0:
            # "o" player won, update game state
            self._game_state = "O_WON"
        # If "o" didn't win, reset win check variable to False and allowed moves to 0
        self._O_WON_check = False
        self._allowed_moves = 0
        # "o" player move was allowed, returns True
        return True

    # The rest of the code is optional (for graders!)
    def rules(self):
        """
        _______________________________________________
        WELCOME TO A GAME OF FBOARD!!!
        FBoard is a game where the 'x' player is trying
        to get to row 7 (row 8 in get_board method) and
        the 'o' player is trying to make it so that 'x'
        player has no allowed moves.

        'x' player can only move diagonally and 'o'
        player can only move diagonally such that the
        row value isn't increasing.

        "The players are restricted to an 8x8 board,
        and players can't occupy the same position.
        _______________________________________________
        """
        return

    def get_board(self):
        """
        Displays board and game state in console, labeling and numbering rows and columns
        (for non-coders 1-8 row or columns makes more sense)
        Prompts user to designate whether they are "x" or "o",
        asks for the inputs required for move_x or move_o functions respectively
        Finally, calls the get_board function again.
        :return:
        """
        print("                         COLUMNS")
        print(str("     ") + str("     1    2    3    4    5    6    7    8"))
        for i in range(8):
            if 1 < i < 6:
                x_label = "ROWS"
                print("    " + x_label[i - 2] + " " + str(i + 1) + " " + str(self._board[i]))
            else:
                print("      " + str(i + 1) + " " + str(self._board[i]))
        print("    Game State: " + self._game_state)
        player = input("    player: x or o?")
        if player.lower() == "x":
            self.move_x(int(input("      To row(1-8): ")) - 1, int(input("      To column(1-8): ")) - 1)
        if player.lower() == "o":
            current_location = [int(input("      From row(1-8): ")) - 1, int(input("      From column(1-8): ")) - 1,
                                int(input("      To row(1-8): ")) - 1, int(input("      To column(1-8): ")) - 1]
            self.move_o(current_location[0], current_location[1], current_location[2], current_location[3])
        # Loop get board method again
        return self.get_board()


# To Initialize test of Class FBoard()
game = FBoard()
help(game.rules)
game.get_board()

