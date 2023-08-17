from starlette.testclient import TestClient

from main import app
from models import PlayerEnum
from test_main import make_move

client = TestClient(app)

def test_win_horizontal():
    """ Winning combination NAUGH take 0th row """
    # reset board
    client.get("/reset")

    response = make_move(PlayerEnum.NAUGHT, 0, 0)
    assert response.json()['winner'] is None

    response = make_move(PlayerEnum.CROSS, 0, 1)
    assert response.json()['winner'] is None

    response = make_move(PlayerEnum.NAUGHT, 1, 0)
    assert response.json()['winner'] is None

    response = make_move(PlayerEnum.CROSS, 2, 2)
    assert response.json()['winner'] is None

    response = make_move(PlayerEnum.NAUGHT, 2, 0)
    assert response.json()['winner'] == PlayerEnum.NAUGHT


def test_win_vertical():
    """ Winning combination NAUGH take 0th column """
    # reset board
    client.get("/reset")

    response = make_move(PlayerEnum.NAUGHT, 0, 0)
    assert response.json()['winner'] is None

    response = make_move(PlayerEnum.CROSS, 2, 2)
    assert response.json()['winner'] is None

    response = make_move(PlayerEnum.NAUGHT, 0, 1)
    assert response.json()['winner'] is None

    response = make_move(PlayerEnum.CROSS, 2, 0)
    assert response.json()['winner'] is None

    response = make_move(PlayerEnum.NAUGHT, 0, 2)
    assert response.json()['winner'] == PlayerEnum.NAUGHT

def test_move_after_win():
    """ Winning combination NAUGH take 0th row and them wrong move """
    # reset board
    client.get("/reset")

    make_move(PlayerEnum.NAUGHT, 0, 0)
    make_move(PlayerEnum.CROSS, 2, 2)
    make_move(PlayerEnum.NAUGHT, 0, 1)
    make_move(PlayerEnum.CROSS, 2, 0)
    response = make_move(PlayerEnum.NAUGHT, 0, 2)
    assert response.json()['winner'] == PlayerEnum.NAUGHT

    # extra move fails
    response = make_move(PlayerEnum.CROSS, 1, 1)
    assert response.status_code == 400


def test_diagonal_win():
    """ Winning combination CROSS takes diagonal """
    # reset board
    client.get("/reset")

    response = make_move(PlayerEnum.CROSS, 0, 0)
    assert response.json()['winner'] is None

    response = make_move(PlayerEnum.NAUGHT, 0, 2)
    assert response.json()['winner'] is None

    response = make_move(PlayerEnum.CROSS, 1, 1)
    assert response.json()['winner'] is None

    response = make_move(PlayerEnum.NAUGHT, 1, 0)
    assert response.json()['winner'] is None

    response = make_move(PlayerEnum.CROSS, 2, 2)
    assert response.json()['winner'] == PlayerEnum.CROSS


def test_diagonal_win():
    """ Winning combination NAUGHT takes another diagonal """
    # reset board
    client.get("/reset")

    response = make_move(PlayerEnum.NAUGHT, 1, 1)
    assert response.json()['winner'] is None

    response = make_move(PlayerEnum.CROSS, 0, 0)
    assert response.json()['winner'] is None

    response = make_move(PlayerEnum.NAUGHT, 0, 2)
    assert response.json()['winner'] is None

    response = make_move(PlayerEnum.CROSS, 0, 1)
    assert response.json()['winner'] is None

    response = make_move(PlayerEnum.NAUGHT, 2, 0)
    print(response.text)
    assert response.json()['winner'] == PlayerEnum.NAUGHT