""" Game related class """
from models import PlayerMove, PlayerEnum, WinnerEnum
import variables


class InvalidMove(BaseException):
    """ Invalid mode exception """


class NotHisTurn(BaseException):
    """ Not player turn exception """


class GameBoard():
    """ Game board clas """
    @staticmethod
    def reset_state():
        """ Reset board state """
        variables.game_field = variables.INITIAL_GAME_STATE.copy()
        variables.game_moves = []

    def move(self, player_move: PlayerMove):
        """ Make move """
        if not self.is_valid_move(player_move):
            raise InvalidMove('This is not a valid move')

        if not self.is_player_turn(player_move):
            raise NotHisTurn('Not his turn ')

        variables.game_field[player_move.y_position][player_move.x_position] = player_move.player
        variables.game_moves.append(player_move)

    def is_player_turn(self, player_move: PlayerMove):
        """ Check if it is a player turn """
        # no previous moves - its ok
        if len(variables.game_moves) == 0:
            return True

        # check last move - is it from same player?
        if variables.game_moves[-1].player == player_move.player:
            return False

        return True

    def is_valid_move(self, player_move: PlayerMove):
        """ Check if it is a valid move """
        # if position occupied - move is invalid
        if variables.game_field[player_move.y_position][player_move.x_position] != '_':
            return False

        return True

    def get_winner(self):
        """ Identify winner """
        for player in [PlayerEnum.CROSS, PlayerEnum.NAUGHT]:
            if (self.check_row_win(player)
                    or self.check_col_win(player) or self.check_diag_win(player)):
                return player
        # if there are empty moves - return None
        if self.has_empty_moves():
            return None

        # if not empty moves
        return WinnerEnum.DRAW

    def check_row_win(self, player: PlayerEnum):
        """ Identify winner by horizontal row """
        win = False
        # check every row in board
        for row in variables.game_field:
            # hope row is winning
            win = True
            for cell in row:
                if cell != player:
                    # unfortunately not a match in a row
                    win = False
                    continue
        return win

    def check_col_win(self, player: PlayerEnum):
        """ Identify winner by column row """
        if player.NAUGHT:
            pass
        return False

    def check_diag_win(self, player: PlayerEnum):
        """ Identify winner by diagonal """
        if player.NAUGHT:
            pass
        return False

    def has_empty_moves(self):
        """ Check if board has empty cells """
        # game board has empty cells
        for row in variables.game_field:
            for cell in row:
                if cell == '_':
                    return True
        return False

    @staticmethod
    def get_state():
        """ Game board state """
        return variables.game_field
