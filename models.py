""" Pydantic model definitions """
from enum import StrEnum
from pydantic import BaseModel


class PlayerEnum(StrEnum):
    """ Player values """
    CROSS = 'X'
    NAUGHT = 'O'

class WinnerEnum(StrEnum):
    """ Winner values """
    CROSS = 'X'
    NAUGHT = 'O'
    DRAW = 'Draw'


class BoardState(BaseModel):
    """ Board state model """
    board: list[list] = []
    winner: WinnerEnum | None = None

class PlayerMove(BaseModel):
    """ Move model """
    player: PlayerEnum
    location: list[int]

    @property
    def x_position(self):
        """ X position of move """
        # x is a first coordinate
        return self.location[0]

    @property
    def y_position(self):
        """ Y position of move """
        # y is a second coordinate
        return self.location[1]
