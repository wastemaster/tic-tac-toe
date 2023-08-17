""" Main program """
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import variables
import game
from models import BoardState, PlayerMove

app = FastAPI()
templates = Jinja2Templates(directory="templates")
the_game = game.GameBoard()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Index page
    """
    return templates.TemplateResponse("index.html",
                                      {
                                          "request": request,
                                          "game_field": variables.game_field,
                                          'game_moves': variables.game_moves,
                                          'winner': the_game.get_winner()})


@app.post("/move")
async def move(player_move: PlayerMove) -> BoardState:
    """ Make move """
    try:
        the_game.move(player_move)
    except (game.InvalidMove, game.NotHisTurn, game.GameEnded) as exception:
        raise HTTPException(status_code=400, detail=str(exception)) from exception

    # return state
    board_state = BoardState(board=the_game.get_state(),
                             winner=the_game.get_winner())
    return board_state


@app.get("/board")
async def board() -> BoardState:
    """ Returns board state """
    board_state = BoardState(board=the_game.get_state(),
                             winner=the_game.get_winner())
    return board_state


@app.get("/reset")
async def reset() -> BoardState:
    """ Reset game state """
    the_game.reset_state()
    board_state = BoardState(board=the_game.get_state(),
                             winner=the_game.get_winner())
    return board_state
